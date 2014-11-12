import os
import sys

os.environ.setdefault("AIDXP_DJANGO_SETTINGS_MODULE", "aid_explorer.settings")

import django.conf
django.conf.ENVIRONMENT_VARIABLE = "AIDXP_DJANGO_SETTINGS_MODULE"

from django.conf import settings
sys.path.append(settings.PREFIX + '/django_files')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
