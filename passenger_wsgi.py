# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1551250/data/www/sto-gs.ru/autogarant')
sys.path.insert(1, '/var/www/u1551250/data/autogarant_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'autogarant.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()