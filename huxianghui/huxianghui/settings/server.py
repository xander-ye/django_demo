from settings import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # mysql database setting:
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huxianghui_db',
        'USER': 'root',
        'PASSWORD': 'qwerasdf',
        'HOST': '',
        'PORT': 3306,
        'OPTIONS': {

        }
    }
}

