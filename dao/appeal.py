from datetime import datetime

from cms.models import Appeal
from dao.auth import AuthManager


class AppealManager:

    @staticmethod
    def get_all():
        appeals = Appeal.objects.all()
        return appeals

    @staticmethod
    def create(text, base_user):
        appeal = Appeal()
        appeal.text = text
        appeal.date = datetime.now()
        appeal.author = AuthManager.get_by_base_user(base_user)
        appeal.save()
