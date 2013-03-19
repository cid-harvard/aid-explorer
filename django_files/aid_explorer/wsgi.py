import os, sys

import django.conf
django.conf.ENVIRONMENT_VARIABLE = "AIDXP_DJANGO_SETTINGS_MODULE"

os.environ.setdefault("AIDXP_DJANGO_SETTINGS_MODULE", "aid_explorer.settings")

sys.path.append('/srv/www/aid_explorer/django_files')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
