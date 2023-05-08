from django.contrib import admin
from .models import *


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
