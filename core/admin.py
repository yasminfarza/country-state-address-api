from django.contrib import admin

from core.models import Country, State, Address

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Address)
