from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Instalacion)
class InstalacionAdmin(admin.ModelAdmin):
    list_display = ['name', 'categoria']


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ['instalacion', 'img']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']
