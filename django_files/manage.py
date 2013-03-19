#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    import django.conf
    django.conf.ENVIRONMENT_VARIABLE = "AIDXP_DJANGO_SETTINGS_MODULE"

    os.environ.setdefault("AIDXP_DJANGO_SETTINGS_MODULE", "aid_explorer.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
