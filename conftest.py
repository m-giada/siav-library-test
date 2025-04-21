import os
import django
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
