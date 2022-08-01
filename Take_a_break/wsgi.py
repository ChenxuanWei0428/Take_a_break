"""
WSGI config for My_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/opt/python/current/app')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Take_a_break.settings')

os.environ["DJANGO_SETTINGS_MODULE"] = "Take_a_break.settings" 

application = get_wsgi_application()