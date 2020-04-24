from django.conf import settings

# Подключение кастомных классов
# empty

# глобальные объекты и переменные
SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS


# обновление значения поля (для автозаполнения)
def update_field(field, value):
    field.widget.attrs.update({ 'value': value })

