from django.contrib import admin

from .models import Trip, Guideline, Restriction, Airline

admin.site.register(Trip)
admin.site.register(Guideline)
admin.site.register(Restriction)
admin.site.register(Airline)