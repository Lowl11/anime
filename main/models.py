from django.db import models

# Пункты навигационной панели
class NavigationLink(models.Model):
    name = models.CharField(max_length = 255, null = False)
    url = models.CharField(max_length = 999, null = False)

    def __str__(self):
        return self.name
    
