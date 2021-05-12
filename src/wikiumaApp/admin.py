from django.contrib import admin
from .models import *
# Register your models here.
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#modeladmin-objects


class CentroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha"]
    search_fields = ["nombre"]


class GradoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha"]
    search_fields = ["nombre"]


class ValoracionAsignaturaAdmin(admin.ModelAdmin):
    list_display = ["asignatura", "reportado"]
    search_fields = ["nombre"]


models = [
    Profesor,
    Asignatura,
    ValoracionProfesor,
    ProfesorAsignatura,
]

models_custom = [
    (Centro, CentroAdmin),
    (Grado, GradoAdmin),
    (ValoracionAsignatura, ValoracionAsignaturaAdmin)
]

for m in models:
    admin.site.register(m)

for (m, c) in models_custom:
    admin.site.register(m, c)
