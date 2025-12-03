import os
from pathlib import Path

# 📍 Đường dẫn gốc của project
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚙️ Cấu hình cơ bản
SECRET_KEY = 'django-insecure-your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 🧩 Các app được cài đặt
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App chính
    'workflow',

    # ✅ Thêm Django REST Framework (cho API)
    'rest_framework',
]

# 🔒 Middleware mặc định của Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ⚙️ URL chính
ROOT_URLCONF = 'qlda_web.urls'

# 🎨 Template hiển thị HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # chứa các file .html
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

# 🔥 Ứng dụng chính của Django
WSGI_APPLICATION = 'qlda_web.wsgi.application'

# ===================================================
# 🗄️ Cấu hình DATABASE MongoDB (thông qua Djongo)
# ===================================================
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'QLDA-GK',  # ✅ tên database trong MongoDB Compass
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://127.0.0.1:27017',  # ✅ host mặc định MongoDB local
        },
    }
}

# 🔑 Kiểm tra mật khẩu
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Ngôn ngữ & múi giờ
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

# 🖼️ Static & Media
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🧱 Kiểu ID mặc định
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ======================================
# 🔐 Cấu hình LOGIN / LOGOUT redirect
# ======================================
LOGIN_URL = 'login'              # ✅ Sửa lỗi /accounts/login/
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# ======================================
# ⚙️ Cấu hình Django REST Framework
# ======================================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
