from django.contrib import admin
from Solcito.models import Student, RegistrationS, Tutor, Assistance, Discipline, Curso, Marks, Subject, RegistrationD, Teacher
# Register your models here.
from Solcito.forms import RegistrationSForm


admin.site.register(Student)
class TutorAdmin(admin.ModelAdmin):
    search_fields = ['children__name','name']

admin.site.register(Tutor,TutorAdmin)

class RegistrationSAdmin(admin.ModelAdmin):
    search_fields = ['student__name']
    form = RegistrationSForm
    list_filter = (['activeDate', 'desactiveDate','curso__curso','curso__division','curso__cycle'])

admin.site.register(RegistrationS,RegistrationSAdmin)

class AssistanceAdmin(admin.ModelAdmin):
    search_fields = ['reg__student__name']
    list_filter = (['reg__student__name','reg__curso__curso','reg__curso__division'])


admin.site.register(Assistance,AssistanceAdmin)

class DisciplineAdmin(admin.ModelAdmin):
    search_fields = ['reg__student__name']
    list_filter = (['reg__student__name','reg__curso__curso','reg__curso__division'])

admin.site.register(Discipline, DisciplineAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_filter = (['curso','division','cycle'])
    exclude = ('idCurso',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(RegistrationD)
admin.site.register(Teacher)
