from django.contrib import admin
from .models import *

admin.site.register([Kino, User, Zhanr, ZhanrKino, Studio, KinoType])
