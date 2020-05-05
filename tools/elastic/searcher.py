import json

from tools.elastic.index import IndexManager
from dao.anime import AnimeManager

class Searcher:
    def __init__(self, talker):
        self.talker = talker
    
    def search_anime(self, query):
        # REST данные
        postfix = self.__anime_index_name() + '/_search'
        request_type = 'POST'

        # данные по поиску
        fields = ['title_rus', 'title_foreign', 'description']
        data = {}
        data['query'] = self.__build_multi_match(query, fields)
        data['suggest'] = self.__build_suggestions(query, fields)

        json_response = self.talker.talk(postfix, data, request_type)

        if json_response is None:
            return json_response
        
        out_hits = json_response['hits']
        inside_hits = out_hits['hits']

        anime_list = []
        for hit in inside_hits:
            anime = hit['_source']
            anime_list.append(AnimeManager.parse(anime))
        
        if len(inside_hits) == 0:
            suggest = json_response['suggest']

            description_suggestions = suggest['description_suggestion']
            title_rus_suggestions = suggest['title_rus_suggestion']
            title_foreign_suggestions = suggest['title_foreign_suggestion']

            description_options = description_suggestions[0]['options']
            title_rus_options = title_rus_suggestions[0]['options']
            title_foreign_options = title_foreign_suggestions[0]['options']

            description_query = { 'score': 0 }
            title_rus_query = { 'score': 0 }
            title_foreign_query = { 'score': 0 }

            if len(description_options) > 0:
                description_query = description_options[0]
            
            if len(title_rus_options) > 0:
                title_rus_query = title_rus_options[0]
            
            if len(title_foreign_options) > 0:
                title_foreign_query = title_foreign_options[0]
            
            biggest = title_rus_query
            if biggest['score'] < title_foreign_query['score']:
                biggest = title_foreign_query
            
            if biggest['score'] < description_query['score']:
                biggest = description_query
            
            if biggest['score'] > 0:
                return self.search_anime(biggest['text'])

        return anime_list
    
    def __anime_index_name(self):
        return IndexManager.anime_index_name()
    
    def __build_multi_match(self, query, fields):
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
        suggestions = {}
        for field in fields:
            suggestions[field + '_suggestion'] = self.__text_field(field, query)
        return suggestions
    
    def __text_field(self, field_name, query):
        text_field = {
            'text': query,
            'term': {
                'field': field_name
            }
        }
        return text_field

