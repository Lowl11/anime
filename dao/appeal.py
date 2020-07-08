from datetime import datetime

from cms.models import Appeal
from dao.auth import AuthManager
from dao.base import BaseDaoManager


class AppealManager(BaseDaoManager):

    def __init__(self):
        super(AppealManager, self).__init__(Appeal, None)

    @staticmethod
    def create(text, base_user):
        appeal = Appeal()
        appeal.text = text
        appeal.date = datetime.now()
        appeal.author = AuthManager.get_by_base_user(base_user)
        appeal.save()
