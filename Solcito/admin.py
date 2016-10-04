from django.contrib import admin
from Solcito.models import Student, RegistrationS, Tutor, Assistance, Discipline, Curso, Marks, Subject, RegistrationD, Teacher
# Register your models here.



admin.site.register(Student)
admin.site.register(Tutor)

class RegistrationSAdmin(admin.ModelAdmin):

    list_filter = ('activeDate', 'curso')


admin.site.register(RegistrationS,RegistrationSAdmin)
admin.site.register(Assistance)
admin.site.register(Discipline)
admin.site.register(Curso)
admin.site.register(Marks)
admin.site.register(Subject)
admin.site.register(RegistrationD)
admin.site.register(Teacher)
