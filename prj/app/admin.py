from django.contrib import admin
from .models import Person, Job, Workshop

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass