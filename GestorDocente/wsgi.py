# wsgi.py placeholder
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GestorDocente.settings')

application = get_wsgi_application()