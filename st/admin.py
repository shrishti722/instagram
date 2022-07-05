
from django.contrib import admin

from aaa.settings import BASE_DIR

# Register your models here.
from .models import employee
admin.site.register(employee)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'