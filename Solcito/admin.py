from django.contrib import admin
from Solcito.models import Student, Registration, Imagen
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('nameStudent',)
    list_display = ('nameStudent','lastNameStudent','_get_foto')

    def _get_foto(self, obj):
         return obj.get_foto()
    _get_foto.allow_tags = True

class RegistrationAdminFoto(admin.ModelAdmin):
    exclude = ()
    list_display = ('photo',)

    def _get_foto(self, obj):
         return obj.get_foto()
    _get_foto.allow_tags = True

admin.site.register(Student)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Imagen, RegistrationAdminFoto)
