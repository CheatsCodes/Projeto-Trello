from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'
ROOT_URLCONF = 'core.urls'  # <-- Adicione esta linha
WSGI_APPLICATION = 'core.wsgi.application'

INSTALLED_APPS = [
    # Apps padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # <-- ESSENCIAL
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Apps de terceiros
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    # Seus apps
    'tasks',
    'users',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pasta global de templates
        'APP_DIRS': True,  # Permite que o Django encontre templates nos apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ESSENCIAL
                'django.contrib.auth.context_processors.auth',  # ESSENCIAL
                'django.contrib.messages.context_processors.messages',  # ESSENCIAL
            ],
        },
    },
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'APP': {
            'client_id': 'SEU_CLIENT_ID_GOOGLE.apps.googleusercontent.com',
            'secret': 'SEU_SECRET_GOOGLE',
            'key': ''
        }
    },
    'github': {
        'SCOPE': ['user:email'],
        'APP': {
            'client_id': 'SEU_CLIENT_ID_GITHUB',
            'secret': 'SEU_SECRET_GITHUB',
        }
    }
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_db',          # Nome do banco de dados
        'USER': 'postgres',         # Usuário do PostgreSQL
        'PASSWORD': '101202',       # Senha (evite caracteres especiais)
        'HOST': 'localhost',        # Banco está na sua máquina
        'PORT': '5432',             # Porta padrão
        'OPTIONS': {
            'client_encoding': 'UTF8'  # Adicione esta linha
        },
    }
}

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = 's_xt)islfx4vk13bfz(8j-f3o(&)b5ytto=qi^8+bs=cp(fkql'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'