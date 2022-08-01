"""
WSGI config for My_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_web.settings')

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings" 

application = StaticFilesHandler(get_wsgi_application())