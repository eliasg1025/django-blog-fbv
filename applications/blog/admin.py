from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        models = Categoria


class AutorResource(resources.ModelResource):
    class Meta:
        models = Autor


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResource


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResource


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Autor)
