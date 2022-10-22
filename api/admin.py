from django.contrib import admin

# Register your models here.
from api.models import Person, Vehicle

"""
Registering the models in admin view
"""
admin.site.register(Person)
admin.site.register(Vehicle)
