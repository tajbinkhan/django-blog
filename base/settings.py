"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR/ 'templates'
STATIC_DIR = BASE_DIR/ 'static'
STATIC_ROOT = BASE_DIR/ 'staticfiles'
MEDIA_ROOT = BASE_DIR/ 'media'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'evankhan.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# My Apps
	'blog.apps.BlogConfig',
	'user.apps.UserConfig',
	'search.apps.SearchConfig',
	'site_setting.apps.SiteSettingConfig',

	# Installed Apps
	'crispy_forms',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook',
	'allauth.socialaccount.providers.google',
	'import_export',
	'ckeditor',
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

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [TEMPLATE_DIR],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
				'blog.context_processors.sidebar',
			],
		},
	},
]

WSGI_APPLICATION = 'base.wsgi.application'

AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_FORMS = {
	'login': 'user.forms.CustomLoginForm',
	'signup': 'user.forms.CustomSignupForm',
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'account_login'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_USE_TLS = True
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Shortcodes
ADMIN_PANEL = 'admin'

# Django All Auth Settings
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION  = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
ACCOUNT_MAX_EMAIL_ADDRESSES = 2
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_SIGNUP_REDIRECT_URL = "account_login"
SOCIALACCOUNT_EMAIL_VERIFICATION = False


CKEDITOR_CONFIGS = {
	'default': {
			# 'skin': 'Kama',
			# 'skin': 'office2013',
			'sourceTextColor': '#000',
			'toolbar_Basic': [
				['Source', '-', 'Bold', 'Italic']
			],
			'toolbar_YourCustomToolbarConfig': [
					{'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
					{'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
					{'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
					{'name': 'forms',
						'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField']},
					'/',
					{'name': 'basicstyles',
						'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
					{'name': 'paragraph',
						'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
											'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
											'Language']},
					{'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
					{'name': 'insert',
						'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
					'/',
					{'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
					{'name': 'colors', 'items': ['TextColor', 'BGColor']},
					{'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
					{'name': 'about', 'items': ['About']},
					'/',  # put this to force next toolbar on new line
					{'name': 'yourcustomtools', 'items': [
							# put the name of your editor.ui.addButton here
							'Preview',
							'Maximize',

					]},
			],
			'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
			# 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
			# 'height': 291,
			'width': '100%',
			# 'filebrowserWindowHeight': 725,
			# 'filebrowserWindowWidth': 940,
			# 'toolbarCanCollapse': True,
			# 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
			'tabSpaces': 4,
			'extraPlugins': ','.join([
					'uploadimage', # the upload image feature
					# your extra plugins here
					'div',
					'autolink',
					'autoembed',
					'embedsemantic',
					'autogrow',
					# 'devtools',
					'widget',
					'lineutils',
					'clipboard',
					'dialog',
					'dialogui',
					'elementspath'
			]),
	}
}