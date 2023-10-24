from django.contrib import admin
from .models import Entidad,Comunicado

# Register your models here.

class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo","entidad","fecha_publicacion","fecha_ultima_modificacion")
    list_filter = [("publicado_por",admin.RelatedOnlyFieldListFilter),]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.publicado_por = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Entidad)
admin.site.register(Comunicado,ComunicadoAdmin)

