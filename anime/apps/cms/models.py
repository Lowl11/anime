from django.db import models
from a_auth.models import Viewer


class CmsMainInfo(models.Model):
    main_notification = models.TextField('Важное уведомление', default = '')
    mini_notification1 = models.TextField('Уведомление №1', default = '')
    mini_notification2 = models.TextField('Уведомление №2', default = '')

    class Meta:
        verbose_name = 'Основная информация по CMS'
        verbose_name_plural = 'Основная информация по CMS'

    def __str__(self):
        return 'Основная информация по CMS'


class CmsNavigationLink(models.Model):
    name = models.CharField(max_length = 255, null = False)
    url = models.CharField(max_length = 999, null = False)
    order_number = models.IntegerField(default = 0)
    glyph_icon = models.CharField(max_length = 255, null = True)

    class Meta:
        verbose_name = 'Навигационная ссылка CMS'
        verbose_name_plural = 'Навигационные ссылки CMS'

    def __str__(self):
        return self.name + ' [' + str(self.order_number) + ']'


class Folder(models.Model):
    name = models.CharField(max_length = 255, null = False)
    parent = models.ForeignKey("cms.Folder", null = True, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length = 255, null = False)
    path = models.CharField(max_length = 999, null = False)
    folder = models.ForeignKey(Folder, null = True, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    
    def __str__(self):
        return self.name


class Appeal(models.Model):
    author = models.ForeignKey(Viewer, models.SET_NULL, null = True, blank = True)
    text = models.TextField('Текст обращения')
    date = models.DateTimeField('Дата обращения')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return 'Обращение от ' + str(self.author) + ' [' + str(self.date) + ']'
