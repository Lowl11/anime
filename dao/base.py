from django.db.models.base import ModelBase

from tools import logger


class BaseDaoManager:
    """ Абстрактный класс для всех моделей БД """

    def __init__(self, model_type: ModelBase, preparation_method):
        self._model_type = model_type
        self._preparation_method = preparation_method

    def get_all(self):
        record_list = self._model_type.objects.all()
        return self._preparation_method(record_list)

    def get_by_id(self, pk: int):
        record = self._model_type.objects.get(pk=pk)
        return record

