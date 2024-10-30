from django.contrib import admin
from weather.models import City

@admin.register(City)
class PrjectAdmin(admin.ModelAdmin):
    list_display = ["name"]