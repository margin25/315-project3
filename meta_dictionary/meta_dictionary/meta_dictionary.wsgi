import os
import sys


path = '/315-project3/meta_dictionary/meta_dictionary'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'meta-dictionary.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()