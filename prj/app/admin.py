from django.contrib import admin
from .models import Person, Artwork, Gallery, Job, Workshop


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_year', 'death_year', 'job', 'workshop']
    search_fields = ['name']


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'creator', 'gallery']
    search_fields = ['name', 'material']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']