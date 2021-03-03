"""
WSGI config for admingroup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Bloco WhiteNoise para Heroku
'''from whitenoise import WhiteNoise

from my_project import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')'''
# Final do bloco
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admingroup.settings.base')

application = get_wsgi_application()
