from django.contrib import admin
from .models import *
# Register your models here.


class CentroAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]


class GradoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]


admin.site.register(Centro, CentroAdmin)
admin.site.register(Grado, GradoAdmin)
