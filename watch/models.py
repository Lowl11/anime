from django.db import models

class Anime(models.Model):
    title_rus = models.CharField(max_length = 255)
    title_foreign = models.CharField(max_length = 255, default = '')
    image = models.ImageField(upload_to = 'anime')

    def __str__(self):
        return self.title_rus
    
