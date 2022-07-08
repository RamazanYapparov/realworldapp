from django.contrib import admin
from .models import *

# Register your models here.
for m in [Actor, Director, Character, Movie]:
    admin.site.register(m)


