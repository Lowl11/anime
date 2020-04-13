from django.db import models

class Anime(models.Model):
    title_rus = models.CharField(max_length = 255)
    title_foreign = models.CharField(max_length = 255, default = '')
    season = models.IntegerField(default = 1)
    image = models.ImageField(upload_to = 'anime')

    def __str__(self):
        if len(self.title_foreign) > 0:
            slash = ' / '
        return self.title_rus + slash + self.title_foreign + ' [TV-' + str(self.season) + ']'
