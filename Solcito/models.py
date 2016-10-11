from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db.models import ImageField
from django.db.models.fields.files import FileField
from ITSGestion.settings import MEDIA_ROOT
# Create your models here.

sex = (
    ("M", "Masculino"),
    ("F", "Femenino"),
    ("O", "Otro")
)
religion = (
    ("cat", "Catolicismo"),
    ("mus", "Islamismo"),
    ("jud", "Judaismo"),
    ("pro", "Protestantismo"),
    ("eva", "Evangelismo"),
    ("ind", "Induismo"),
    ("bud", "Budismo"),
    ("agn", "Agnosticismo"),
    ("otr", "Other")
)
rol = (
    ("Father", "Father"),
    ("Mother", "Mother"),
    ("Tutor", "Tutor")
)
curso = (
    ('1',"Primero"),
    ('2',"Segundo"),
    ('3',"Tercero"),
    ('4',"Cuarto"),
    ('5',"Quinto"),
    ('6',"Sexto"),
    ('7',"Septimo")
)
division = (
    ('A',"A"),
    ('B',"B"),
    ('C',"C")
)
nota = (
    ('1',"1"),
    ('2',"2"),
    ('3',"3"),
    ('4',"4"),
    ('5',"5"),
    ('6',"6"),
    ('7',"7"),
    ('8',"8"),
    ('9',"9"),
    ('10',"10")
)
trim = (
    ('1',"Primer Trimestre"),
    ('2',"Segundo Trimestre"),
    ('3',"Tercer Trimestre")
)
falta = (
    (1,"1"),
    (0.5,"1/2"),
    (0.25,"1/4")
)
sancion = (
    ("Observacion","Observacion"),
    ("Amonestacion","Amonestacion")
)
teacher = (
    ("teacher","Profesor"),
    ("celador","Preceptor")
)

class Student(models.Model):
    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"

    idStudent = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    lastName = models.CharField(u'Apellido', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    sex = models.CharField(u'Genero', max_length=1, choices=sex, default='M', blank=False)
    religion = models.CharField(u'Religion', max_length=3, choices=religion, default='cat', blank=False)
    birthDate = models.DateField(u'Fecha de Nacimiento', blank=False)
    birthPlace = models.CharField(u'Lugar de Nacimiento', max_length=50, blank=False)
    nacionality = models.CharField(u'Nacionalidad', max_length=50, blank=False)
    street = models.CharField(u'Calle', max_length=50, blank=False)
    numberStreet = models.IntegerField(u'Altura', blank=False)
    neighborhood = models.CharField(u'Barrio', max_length=50, blank=False)
    tower = models.CharField(u'Torre', max_length=20, blank=True, null=True, default="")
    floorDepartment = models.IntegerField(u'Piso', blank=True, null=True, default="")
    department = models.CharField(u'Departamento', max_length=20, blank=True, null=True, default="")
    PC = models.IntegerField(u'Codigo Postal', blank=False)
    nacionality = models.CharField(u'Nacionalidad', max_length=50, blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    landline = models.IntegerField(u'Telefono', blank=False)
    cellphone = models.IntegerField(u'Celular', blank=True, null=True, default="")
    curso = models.CharField(u'Curso a Matricular', max_length=1, choices=curso, default='1', blank=False)

    studentId = models.IntegerField(u'Legajo de Alumno', blank=True , null=True, default="")
    administrativeId = models.IntegerField(u'Legajo Administrativo', blank=True , null=True, default="")
    previousSchool = models.CharField(u'Previous School', max_length=50, blank=True, null=True, default="")
    qDueSubjects = models.IntegerField(u'Due Subjects', blank=True, null=True, default="")

    active = models.BooleanField(u'Matriculado', default=False)

    def __str__(self):
        return self.name

class RegistrationS(models.Model):
    class Meta:
        verbose_name="Matricula"
        verbose_name_plural="Matriculas"

    def __str__(self):
        return self.student.name + " " + str(self.curso.cycle)
    idRegistrationS = models.AutoField(primary_key=True, editable=False)
    activeDate = models.DateField(u'Fecha de Alta', blank=False)
    desactiveDate = models.DateField(u'Fecha de Baja', blank=False)
    student = models.ForeignKey('Student', related_name='ownerregistration')
    curso = models.ForeignKey('Curso', related_name='regincurso')

@receiver(pre_save, sender=RegistrationS)
def create_personal_account(sender, instance, **kwargs):
    if instance._state.adding:
        instance.student.active = True
        instance.student.save()

class Assistance(models.Model):
    class Meta:
        verbose_name="Asistencia"
        verbose_name_plural="Asistencias"

    idAssistance = models.AutoField(primary_key=True, editable=False)
    date = models.DateField(u'Fecha', blank=False)
    tipo = models.FloatField(u'Tipo de Falta', choices=falta, blank=False)
    justify = models.BooleanField(u'Justificada', default=False)
    reg = models.ForeignKey('RegistrationS', related_name='aofReg')
    def __str__(self):
        return str(self.tipo) + " falta del alumno " + self.reg.student.name + " el dia " + str(self.date.day) + " del " + str(self.date.month) + " del " + str(self.date.year)

class Discipline(models.Model):
    class Meta:
        verbose_name="Conducta"
        verbose_name_plural="Conducta"

    idDiscipline = models.AutoField(primary_key=True, editable=False)
    sancion = models.CharField(u'Sancion', choices=sancion, max_length=15, blank=False)
    cant = models.IntegerField(u'Cantidad', default='1', blank=False)
    reg = models.ForeignKey('RegistrationS', related_name='dofReg')
    def __str__(self):
        return self.sancion + " a " + self.reg.student.name

class Curso(models.Model):
    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"

    idCurso = models.AutoField(primary_key=True, editable=False)
    curso = models.CharField(u'Curso', max_length=1, choices=curso, default='1', blank=False)
    division = models.CharField(u'Division', max_length=1, choices=division, default='A', blank=False)
    cycle = models.IntegerField(u'Ciclo Lectivo', default='2016', blank=False)

    def __str__(self):
        return self.curso + " " + self.division + " " + str(self.cycle)

class Marks(models.Model):
    class Meta:
        verbose_name="Nota"
        verbose_name_plural="Notas"

    idMark = models.AutoField(primary_key=True, editable=False)
    nota = models.CharField(u'Nota', max_length=1, choices=nota, blank=False)
    trim = models.CharField(u'Trim', max_length=1, choices=trim, blank=False)
    subject = models.ForeignKey('Subject', related_name='minsubject')
    reg = models.ForeignKey('RegistrationS', related_name='mofReg')

    def __str__(self):
        return  self.reg.student.name + " " + self.reg.student.lastName +  " tiene un " +  self.nota + " en " + self.subject.name

class Subject(models.Model):
    class Meta:
        verbose_name="Materia"
        verbose_name_plural="Materias"

    idSubject = models.AutoField(primary_key=True, editable=False)
    isRedondeable = models.BooleanField(u'Se redondea', default=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    curso = models.ForeignKey('Curso', related_name='ofcurso')


    def __str__(self):
        return self.name + " " + self.curso.curso + " " + self.curso.division


class RegistrationD(models.Model):
    class Meta:
        verbose_name="Matricula Docente"
        verbose_name_plural="Matriculas Docente"

    idRegistrationD = models.AutoField(primary_key=True, editable=False)
    activeDate = models.DateField(u'Fecha de Alta', blank=False)
    desactiveDate = models.DateField(u'Fecha de Baja', blank=False)
    isSustitute = models.BooleanField(u'Titular/Suplente', default=False)
    subject = models.ForeignKey('Subject', related_name='insubject')
    teacher = models.ForeignKey('Teacher', related_name='ownerregistration')

    def __str__(self):
        return self.teacher.name+ " " + self.teacher.lastName + " " + self.subject.name + " " + self.subject.curso.curso + " " + self.subject.curso.division


class Teacher(models.Model):
    class Meta:
        verbose_name="Docente"
        verbose_name_plural="Docente"

    idteacher = models.AutoField(primary_key=True, editable=False)
    authuser = models.OneToOneField(User)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    lastName = models.CharField(u'Apellido', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    cellphone = models.IntegerField(u'Celular', blank=True, null=True, default="")
    tipo = models.CharField(u'Rol', choices=teacher, default='teacher', max_length=7, blank=False)
    def __str__(self):
        return self.name + " " + self.lastName


class Tutor (models.Model):
    class Meta:
        verbose_name="Padre"
        verbose_name_plural="Padres"

    idTutor = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    lastName = models.CharField(u'Apellido', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    cuil = models.IntegerField(u'Cuil', blank=False)
    rol = models.CharField(u'Rol', choices=rol, default='Tutor', blank=False, max_length=10,)
    workPlace = models.CharField(u'Lugar de Trabajo', max_length=50, blank=False)
    profession = models.CharField(u'Profesion', max_length=50, blank=False)
    locality = models.CharField(u'Localidad', max_length=50, default="", blank=False)
    street = models.CharField(u'Calle', max_length=50, blank=False)
    numberStreet = models.IntegerField(u'Altura', blank=False)
    neighborhood = models.CharField(u'Barrio', max_length=50, blank=False)
    tower = models.CharField(u'Torre', max_length=20, blank=True, null=True)
    floorDepartment = models.IntegerField(u'Piso', blank=True, null=True)
    department = models.CharField(u'Departamento', max_length=20, blank=True, null=True)
    PC = models.IntegerField(u'Codigo Postal', blank=False)
    nacionality = models.CharField(u'Nacionalidad', max_length=50, blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    landline = models.IntegerField(u'Telefono Fijo', blank=False)
    cellphone = models.IntegerField(u'Celular', blank=True, null=True)
    workPhone = models.IntegerField(u'Telefono Laboral', blank=True, null=True)
    children = models.ManyToManyField(Student)
    def __str__(self):
        nombre = self.name + " padre de : "
        for i in self.children.all:
            nombre = nombre + self.children.name+  ", "
        return nombre
