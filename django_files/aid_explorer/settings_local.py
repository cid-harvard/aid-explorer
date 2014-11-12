PREFIX = '/Users/makmana/aidxp'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'aidxp_db.sqlite3',                      # Or path to database file if using sqlite3.
    }
}

STATICFILES_DIRS = (
    PREFIX + '/media',
)

SECRET_KEY = '-%vx@ocghp%7a3+@6evdzn#=v071$t-cl6m&4h5^iv#65mt13y'

TEMPLATE_DIRS = (
    PREFIX + '/html',
)

