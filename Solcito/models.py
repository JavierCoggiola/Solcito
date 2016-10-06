from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

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
    ("jud", "Judasimo"),
    ("pro", "Protestantismo"),
    ("eva", "Evangelismo"),
    ("ind", "Induismo"),
    ("bud", "Budismo"),
    ("agn", "Agnosticismo"),
    ("otr", "Other")
)
rol = (
    ("fat", "Father"),
    ("mot", "Mother"),
    ("tut", "Tutor")
)
curso = (
    ('1',"Primero"),
    ('2',"Segundo"),
    ('3',"Tercero"),
    ('4',"Cuarto"),
    ('5',"Quinto"),
    ('6',"Secxtoo"),
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
    ("1", 1),
    ("1/2", 0.5),
    ("1/4", 0.25)
)
sancion = (
    ("obser","Observacion"),
    ("amone","Amonestacion")
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


    def __str__(self):
        return self.name

class RegistrationS(models.Model):
    class Meta:
        verbose_name="Matricula"
        verbose_name_plural="Matriculas"

    def __str__(self):
        return self.student.name + " " + str(self.idRegistrationS)
    idRegistrationS = models.AutoField(primary_key=True, editable=False)
    activeDate = models.DateField(u'Fecha de Alta', blank=False)
    desactiveDate = models.DateField(u'Fecha de Baja', blank=False)
    student = models.ForeignKey('Student', related_name='ownerregistration')
    curso = models.ForeignKey('Curso', related_name='regincurso')



class Assistance(models.Model):
    idAssistance = models.AutoField(primary_key=True, editable=False)
    date = models.DateField(u'Fecha', blank=False)
    tipo = models.FloatField(u'Tipo de Falta', choices=falta, blank=False)
    justify = models.BooleanField(u'Justificada', default=False)
    reg = models.ForeignKey('RegistrationS', related_name='aofReg')
    
class Discipline(models.Model):
    idDiscipline = models.AutoField(primary_key=True, editable=False)
    sancion = models.CharField(u'Sancion', choices=sancion, max_length=5, blank=False)
    cant = models.IntegerField(u'Cantidad', default='1', blank=False)
    reg = models.ForeignKey('RegistrationS', related_name='dofReg')

class Curso(models.Model):
    idCurso = models.AutoField(primary_key=True, editable=False)
    curso = models.CharField(u'Curso', max_length=1, choices=curso, default='1', blank=False)
    division = models.CharField(u'Division', max_length=1, choices=division, default='A', blank=False)
    cycle = models.IntegerField(u'Ciclo Lectivo', default='2016', blank=False)

    def __str__(self):
        return self.curso + " " + self.division + " " + str(self.cycle)

class Marks(models.Model):
    idMark = models.AutoField(primary_key=True, editable=False)
    nota = models.CharField(u'Nota', max_length=1, choices=nota, blank=False)
    trim = models.CharField(u'Trim', max_length=1, choices=trim, blank=False)
    subject = models.ForeignKey('Subject', related_name='minsubject')
    reg = models.ForeignKey('RegistrationS', related_name='mofReg')
        
class Subject(models.Model):
    idSubject = models.AutoField(primary_key=True, editable=False)
    isRedondeable = models.BooleanField(u'Se redondea', default=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    curso = models.ForeignKey('Curso', related_name='ofcurso')
        
class RegistrationD(models.Model):
    idRegistrationD = models.AutoField(primary_key=True, editable=False)        
    activeDate = models.DateField(u'Fecha de Alta', blank=False)
    desactiveDate = models.DateField(u'Fecha de Baja', blank=False)
    isSustitute = models.BooleanField(u'Titular/Suplente', default=False)
    subject = models.ForeignKey('Subject', related_name='insubject')
    teacher = models.ForeignKey('Teacher', related_name='ownerregistration')
        
class Teacher(models.Model):
    idteacher = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    lastName = models.CharField(u'Apellido', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    cellphone = models.IntegerField(u'Celular', blank=True, null=True, default="")
    tipo = models.CharField(u'Rol', choices=teacher, default='teacher', max_length=7, blank=False)

class Tutor (models.Model):

    idTutor = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Nombre', max_length=50, blank=False)
    lastName = models.CharField(u'Apellido', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    cuil = models.IntegerField(u'Cuil', blank=False)
    rol = models.IntegerField(u'Rol', choices=rol, default='fat', blank=False)
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

    def __str__(self):
        return self.name 