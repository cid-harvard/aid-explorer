activate_this = '/srv/www/aid_explorer/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


import os, sys

import django.conf
django.conf.ENVIRONMENT_VARIABLE = "AIDXP_DJANGO_SETTINGS_MODULE"

os.environ.setdefault("AIDXP_DJANGO_SETTINGS_MODULE", "aid_explorer.settings")

sys.path.append('/srv/www/aid_explorer/django_files')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
