from django import forms
from django.conf import settings

# подключение кастомных файлов
from .settings import CmsSettings

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


class ManageAnimeForm(forms.Form):
    title_rus = forms.CharField(label = 'Название на русском', min_length = CONSTANTS['manage_anime_title_min'], max_length = 255)
    title_foreign = forms.CharField(label = 'Название на иностранном', min_length = CONSTANTS['manage_anime_title_min'], max_length = 255)
    season = forms.IntegerField(label = 'Номер сезона', min_value = 0)
    description = forms.CharField(label = 'Описание', widget = forms.Textarea, min_length = CONSTANTS['manage_anime_description_min'])
    episodes_quantity = forms.IntegerField(label = 'Количество серий')
    start_date = forms.DateField(label = 'Дата начала')
    image = forms.ImageField(label = 'Обложка')

    title_rus.widget.attrs.update({'class': 'form-control'})
    title_foreign.widget.attrs.update({'class': 'form-control'})
    season.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control'})
    episodes_quantity.widget.attrs.update({'class': 'form-control'})
    start_date.widget.attrs.update({'class': 'form-control'})
    image.widget.attrs.update({'class': 'form-control'})
