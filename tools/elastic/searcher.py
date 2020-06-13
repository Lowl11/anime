import json

# Подключение кастомных классов
from tools.elastic.index import IndexManager
from dao.anime import AnimeManager
from tools import logger


class Searcher:
    """ Searcher - инструмент для поиска непосредественно по эластику """

    def __init__(self, talker):
        self.talker = talker

    def search_anime(self, query):
        """ поиск аниме """

        # REST данные
        postfix = self.__anime_index_name() + '/_search'
        request_type = 'POST'

        # данные по поиску
        fields = ['title_rus', 'title_foreign', 'description', 'tags']
        data = self.__build_data(query, fields)

        # непосредственно сам запрос
        response, err = self.talker.talk(postfix, data, request_type)

        if err is not None:
            # здесь не нужно логировать ошибку т.к. в talker это уже делается
            return None

        # если поиск прошел успешно
        json_response = response.json()

        # есть коренной объект hits и внутри еще один hits (в котором уже лежат данные)
        out_hits = json_response['hits']
        inside_hits = out_hits['hits']

        # подводим _source объекты к анимешкам
        anime_list = []
        for hit in inside_hits:
            anime = hit['_source']
            anime_list.append(AnimeManager.parse(anime))

        # если поиск по фразе query ничего не дал, то находим suggestion
        # по которому произведем поиск еще раз
        if len(inside_hits) == 0:
            suggestion = self.__find_suggestion(json_response, fields)
            if suggestion is not None:
                anime_list = self.search_anime(suggestion)

        return anime_list

    def __find_suggestion(self, json_response, fields):
        suggest = json_response['suggest']  # коренной объект suggest и в нем suggestion по каждому из полей

        suggestions = []
        for field in fields:
            suggestions.append(suggest[field + '_suggestion'])

        # эластик предлогает варианты основываясь на каждом из полей
        # по этому из каждого поля берем первый вариант (то есть самый вероятный)
        options = []
        for suggestion in suggestions:
            options.append(suggestion[0]['options'])

        # вычисляем самый вероятный вариант из лучших вариантов своих полей
        queries = []
        for option in options:
            if len(option) > 0:
                queries.append(option[0])

        # находим вариант с самым большим кол-вом score
        if len(queries) > 0:
            biggest = queries[0]
            for query in queries:
                if biggest['score'] < query['score']:
                    biggest = query

            if biggest['score'] > 0:  # если есть suggestion возвращаем
                return biggest['text']

        return None

    def __anime_index_name(self):
        """ возвращает актуальное название аниме индекса """

        return IndexManager.anime_index_name()

    def __build_data(self, query, fields):
        data = {
            'query': self.__build_multi_match(query, fields),
            'suggest': self.__build_suggestions(query, fields)
        }
        return data

    def __build_multi_match(self, query, fields):
        """ строит multi_match запрос (тип поиска в эластике) """

        multi_match = {
            'multi_match': {
                'query': query,
                'fields': fields,
                "prefix_length": 2,
                "max_expansions": 1
            }
        }
        return multi_match

    def __build_suggestions(self, query, fields):
        """ строит suggestion'ы (подсказки) для каждого поискового поля """

        suggestions = {}
        for field in fields:
            suggestions[field + '_suggestion'] = self.__text_field(field, query)
        return suggestions

    def __text_field(self, field_name, query):
        """ возвращает тип поля text """

        text_field = {
            'text': query,
            'term': {
                'field': field_name
            }
        }
        return text_field
