### Django 3.0.5

### Подключенные библиотеки
import os

### Базовые и первые настройки
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ для расшифровкий паролей и токенов
SECRET_KEY = '#i)f3^l)5e(uz%44z($mqacm2v%#5agz=rho(@uczoh!(%wgl-'

# Трансформер
DEBUG = True

ALLOWED_HOSTS = []


### Подключение более сложных настроек
# Список подключенных приложений
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'a_auth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Первый файл к которому нужно обращаться при роутинге
ROOT_URLCONF = 'anime.urls'

# Механизм HTML шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'anime.wsgi.application'


# Подключение к базе данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'anime',
        'USER': 'postgres',
        'PASSWORD': 'iamverylazy98',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Дополнительные настройки связанные с локализацией
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Путь к статическим файлам
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

"""
Статические - просто вшитие в проект файлы
Медиа - заливаемые юзерами и самим приложением файлы
"""

# Путь к медиа файлам
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Глобальный массив кастомных настроек используемых по всему проекту
Y_SETTINGS = {
    'debug': DEBUG,
    'debugger': True,
    'preloader': False
}
