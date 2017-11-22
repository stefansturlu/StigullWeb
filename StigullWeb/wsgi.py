"""
WSGI config for StigullWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "StigullWeb.settings"

#from django.contrib.auth.handlers.modwsgi import check_password
#from django.core.handlers.wsgi import WSGIHandler

#application = WSGIHandler()
application = get_wsgi_application()
