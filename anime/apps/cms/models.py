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
