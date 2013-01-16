import os, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aid_explorer.settings")

sys.path.append('/srv/www/aid_explorer/django_files')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
