import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jz44$b3ru2oji%tss&c^avm!c-^t9zjm4dq^0^xl)8cue$s8qh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['flytrip.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'users',
    'hotel',
    'travel_tour',
    'account',
    'rental',
    'restaurant',
    'booking',
    'points',
    # 'weasyprint'
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    # 'grappelli',
    # 'filebrowser',
    # 'tinymce',
    'session_security',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, 'travel/templates')],

        'DIRS': [os.path.join(BASE_DIR, 'travel/templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hotel.context_processors.hotelDashboard',
                'hotel.context_processors.approvalcount',
                'hotel.context_processors.invcount',
                'hotel.context_processors.rentalcount',
                'hotel.context_processors.rentalinvcount',
                'booking.contextprocessors.membershipUpgradesCount',
                'booking.contextprocessors.PartnershipUpgradesCount',
                'hotel.context_processors.restaurantcount',
                'hotel.context_processors.restaurantinvcount',
                # 'travel_tour.context_processors.travelDashboard',
                'travel_tour.context_processors.TravelApprovalCount',
                'travel_tour.context_processors.TourPackageCount',
                # 'hotel.context_processors.hotel_name'
            ],
        },
    },
]

WSGI_APPLICATION = 'travel.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'hotel/media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Costom django auth settings


AUTH_USER_MODEL = 'account.User'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_REDIRECT_URL = 'PropertyDetail'
LOGOUT_REDIRECT_URL = 'login'

EMAIL_USE_TLS = True
EMAIL_HOST = 'codeforcore.com'
EMAIL_HOST_USER = 'flytrip@codeforcore.com'
EMAIL_HOST_PASSWORD = '@codeforcore.com'
EMAIL_PORT = 587

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':
        (
            'rest_framework.permissions.IsAuthenticated',
        ),
}

django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SECURITY_INSECURE = True
SESSION_SECURITY_EXPIRE_AFTER = 30*60
SESSION_SECURITY_WARN_AFTER=20*60

TIME_INPUT_FORMATS = ('%H:%M',)


