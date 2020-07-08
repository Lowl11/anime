from django.db.models.base import ModelBase

from tools import logger


class BaseDaoManager:
    """ Абстрактный класс для всех моделей БД """

    def __init__(self, model_type: ModelBase, preparation_method):
        self._model_type = model_type
        self._preparation_method = preparation_method

    def get_all(self):
        records = self._model_type.objects.all()
        return self.prepare_records(records)

    def get_by_id(self, pk: int):
        record = self._model_type.objects.get(pk=pk)
        return record

    def prepare_records(self, records):
        if self._preparation_method is None:
            return records
        return self._preparation_method(records)

