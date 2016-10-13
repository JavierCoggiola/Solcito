from django.contrib import admin
from Solcito.models import Student, RegistrationS, Tutor, Assistance, Discipline, Curso, Marks, Subject, RegistrationD, Teacher
# Register your models here.
from Solcito.forms import RegistrationSForm, TeacherForm
import datetime


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name','dni']

admin.site.register(Student, StudentAdmin)
class TutorAdmin(admin.ModelAdmin):
    search_fields = ['children__name','name']

admin.site.register(Tutor,TutorAdmin)

class RegistrationSAdmin(admin.ModelAdmin):
    search_fields = ['student__name']
    form = RegistrationSForm
    list_filter = (['activeDate', 'desactiveDate','curso__curso','curso__division','curso__cycle'])

    # Aca filtro solamente los alumnos que no tienen una matricula activa
    # Aca filtro el cursos para que solo pueda elegir entre cursos de este ano
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = Student.objects.filter(active=False)
        if db_field.name == "curso":
            kwargs["queryset"] = Curso.objects.filter(cycle=datetime.datetime.now().year)
        return super(RegistrationSAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(RegistrationS,RegistrationSAdmin)

class AssistanceAdmin(admin.ModelAdmin):
    search_fields = ['reg__student__name']
    list_filter = (['reg__student__name','reg__curso__curso','reg__curso__division'])

    # Aca filtro el campo matriculas para que solo pueda elegir entre las matriculas de este ano
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "reg":
            kwargs["queryset"] = RegistrationS.objects.filter(curso__cycle=datetime.datetime.now().year)
        return super(AssistanceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Assistance,AssistanceAdmin)

class DisciplineAdmin(admin.ModelAdmin):
    search_fields = ['reg__student__name']
    list_filter = (['reg__student__name','reg__curso__curso','reg__curso__division'])

    # Aca filtro el campo matriculas para que solo pueda elegir entre las matriculas de este ano
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "reg":
            kwargs["queryset"] = RegistrationS.objects.filter(curso__cycle=datetime.datetime.now().year)
        return super(DisciplineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Discipline, DisciplineAdmin)

class CursoAdmin(admin.ModelAdmin):

    list_filter = (['curso','division','cycle'])
    default_filters = ('cycle='+str(datetime.datetime.now().year),)
    exclude = ('idCurso',)

admin.site.register(Curso, CursoAdmin)

class MarksAdmin(admin.ModelAdmin):
    search_fields = ['reg__student__lastName', 'reg__student__name', ]
    list_filter = (['subject__name','subject__curso__curso','subject__curso__division','subject__curso__cycle'])
    default_filters = ('subject__curso__cycle=' + str(datetime.datetime.now().year),)
    exclude = ('idMark',)
    list_display = ('reg','subject','nota','trim')
    # Filtro para que el docente solo pueda anadir notas a sus materias
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject":
            try:
                kwargs["queryset"] = Subject.objects.filter(insubject__teacher=request.user.teacher)
            except:
                pass
        if db_field.name == "reg":
            try:
                materias = Subject.objects.filter(insubject__teacher=request.user.teacher)
                kwargs["queryset"] = RegistrationS.objects.filter(curso__ofcurso__idSubject=materias)
            except:
                pass
        return super(MarksAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        '''
        Devuelve solo las notas de las materias que el docente esta matriculado
        '''
        qs = super(MarksAdmin, self).get_queryset(request)
        try:
            materias = Subject.objects.filter(insubject__teacher=request.user.teacher)
            return qs.filter(subject__in=materias)
        except:
            return qs

admin.site.register(Marks, MarksAdmin)
admin.site.register(Subject)
admin.site.register(RegistrationD)

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = TeacherForm
    exclude = ('authuser',)

admin.site.register(Teacher,TeacherAdmin)
