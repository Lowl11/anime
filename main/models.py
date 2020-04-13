from django.db import models

# Пункты навигационной панели
class NavigationLink(models.Model):
    name = models.CharField(max_length = 255, null = False)
    url = models.CharField(max_length = 999, null = False)

    class Meta:
        verbose_name_plural = 'Навигационные ссылки'

    def __str__(self):
        return self.name
    
