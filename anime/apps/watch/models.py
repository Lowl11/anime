from django.db import models

from a_auth.models import Viewer


class Anime(models.Model):
    title_rus = models.CharField('Название на русском', max_length = 255)
    title_foreign = models.CharField('Название на иностранном', max_length = 255, default = '')
    season = models.IntegerField('Номер сезона', default = 1)
    description = models.TextField('Описание', default = '')
    episodes_quantity = models.IntegerField('Количество серий', default = 12)
    start_date = models.DateField('Дата начала', default = '2020-01-01')
    image = models.ImageField('Обложка', upload_to = 'anime')
    tags = models.CharField('Поисковые теги', max_length = 1000, null = True, blank = True)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Список аниме'

    def __str__(self):
        if len(self.title_foreign) > 0:
            slash = ' / '
        return self.title_rus + slash + self.title_foreign + ' [TV-' + str(self.season) + ']'


class AnimeComment(models.Model):
    author = models.ForeignKey(Viewer, models.SET_NULL, null = True, blank = True)
    anime = models.ForeignKey(Anime, models.CASCADE)
    text = models.TextField('Текст комментария')

    class Meta:
        verbose_name = 'Комментарий под аниме'
        verbose_name_plural = 'Комментарии под аниме'

    def __str__(self):
        return str(self.author.base_user) + ' оставил(а) комментарий под ' + str(self.anime)


class ConstantGenre(models.Model):
    name = models.CharField('Название жанра', max_length = 255, unique = True)
    order_number = models.IntegerField('Порядковый номер', unique = True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name + ' [' + str(self.order_number) + ']'


class Genre(models.Model):
    constant_genre = models.ForeignKey(ConstantGenre, on_delete = models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Жанр Аниме'
        verbose_name_plural = 'Жанры Аниме'

    def __str__(self):
        return str(self.anime) + ' - ' + self.constant_genre.name
