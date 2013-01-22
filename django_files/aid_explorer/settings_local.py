DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'aidxp_db',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '1n7ugrzy',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATICFILES_DIRS = (
    '/srv/www/media/aid_explorer',
)

SECRET_KEY = '-%vx@ocghp%7a3+@6evdzn#=v071$t-cl6m&4h5^iv#65mt13y'

TEMPLATE_DIRS = (
    '/srv/www/aid_explorer/html',
)

