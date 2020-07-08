from tools import debugger
from django.db.models.base import ModelBase


class BaseDaoManager:
    def __init__(self, model_type: ModelBase, preparation_method):
        self._model_type = model_type
        self._preparation_method = preparation_method

    def get_all(self):
        result = self._model_type.objects.all()
        return self._preparation_method(result)


