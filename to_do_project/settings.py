import os
import dj_database_url # Dosyanın en üstüne ekle
from pathlib import Path

# Proje dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK: Yayında bu anahtarı gizli tutmalısın
SECRET_KEY = 'django-insecure-p!fo@o==lqfc%!cwvn_c^p8vi%%wje#i)@0+6+v&1el%mcuc1a'

# Hataları görmek için şimdilik True (Site açılınca False yapmalısın)
DEBUG = True

# Render URL'ini ve yereli kapsar
ALLOWED_HOSTS = ['serkan-to-do.onrender.com', '127.0.0.1', 'localhost', '.onrender.com']

# Uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks', # Senin uygulaman
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Statik dosyalar için Render'da gerekli
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'to_do_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'to_do_project.wsgi.application'



# Veritabanı ayarı
DATABASES = {
    'default': dj_database_url.config(
        # Render'daki 'DATABASE_URL' isimli ortam değişkenine bakar
        # Eğer bulamazsa (yereldeysen) SQLite kullanır
        default=os.environ.get('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
        conn_max_age=600
    )
}

# Şifre Doğrulama
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Dil ve Zaman Ayarı (Türkiye'ye göre ayarlandı)
LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# Statik Dosya Ayarları (Render İçin Kritik)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Statik dosyaların sunulması için WhiteNoise ayarı
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'