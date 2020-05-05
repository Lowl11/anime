from django.db import models

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
    
