from django.contrib import admin
from .models import *

admin.site.register([Kino, Zhanr, ZhanrKino, Studio, KinoType])
