from django.db.models.base import ModelBase

from tools import logger
from tools import debugger


MAX_RECORDS_SIZE = 100


class BaseDaoManager:
    """ Абстрактный класс для всех моделей БД """

    def __init__(self, model_type: ModelBase, preparation_method=None):
        self._model_type = model_type
        self._preparation_method = preparation_method

    def get_all(self):
        records = self.__all()
        return self.__prepare_records(records)

    def get_by_id(self, pk: int):
        try:
            record = self._model_type.objects.get(pk=pk)
        except Exception as error:
            logger.write('Ошибка поиска модели "' + str(self._model_type) + '". Сообщение: ' + str(error), logger.DAO)
        return record

    @staticmethod
    def save(record: ModelBase):
        record.save()

    def __prepare_records(self, records):
        if self._preparation_method is None:
            return records
        return self._preparation_method(records)[:MAX_RECORDS_SIZE]

    def __all(self):
        records = self._model_type.objects.all()
        return records

