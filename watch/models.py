from django.db import models

class Anime(models.Model):
    title_rus = models.CharField('Название на русском', max_length = 255)
    title_foreign = models.CharField('Название на иностранном', max_length = 255, default = '')
    season = models.IntegerField('Номер сезона', default = 1)
    description = models.TextField('Описание', default = '')
    episodes_quantity = models.IntegerField('Количество серий', default = 12)
    start_date = models.DateField('Дата начала', default = '2020-01-01')
    genre_list = models.CharField(max_length = 999, default = '')
    image = models.ImageField('Обложка', upload_to = 'anime')

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Список аниме'

    def __str__(self):
        if len(self.title_foreign) > 0:
            slash = ' / '
        return self.title_rus + slash + self.title_foreign + ' [TV-' + str(self.season) + ']'

class Genre(models.Model):
    name = models.CharField('Название жанра', max_length = 255)
    order_number = models.IntegerField('Порядковый номер')

    class Meta:
        verbose_name = 'Жанр Аниме'
        verbose_name_plural = 'Жанры Аниме'

    def __str__(self):
        return self.name + ' [' + str(self.order_number) + ']'
