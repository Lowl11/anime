from django.db import models

# Пользователь
class Viewer(models.Model):
    base_user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'users')

    # Регистрация базового пользователя джанго
    def signup_base_user(self, username, password, first_name, last_name):
        base_user = User()
        base_user.username = username
        base_user.set_password(password)
        base_user.first_name = first_name
        base_user.last_name = last_name
        self.base_user = base_user
        self.base_user.save()

    def __str__(self):
        return self.base_user.username
