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
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
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
    ("tut", "Tutor"),
)

class Student(models.Model):
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

    def __str__(self):
        return self.name
    
    def get_foto(self):
        try:
            name = "photos/{}-{}-{}".format(self.name,self.lastName,self.dni)
            img = Imagen.objects.filter(photo__startswith = name)
            if img.count()>0:
                return img.first()
        except Exception as e:
            return None 
    
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

class Registration(models.Model):
    idRegistration = models.AutoField(primary_key=True, editable=False)
    studentFile = models.IntegerField(u'Student File', blank=True , null=True, default="")
    administrativeFile = models.IntegerField(u'Administrative File', blank=True , null=True, default="")
    grade = models.IntegerField(u'Grade', blank=True , null=True, default="")
    division = models.CharField(u'Division', max_length=1, blank=True , null=True, default="")
    previousSchool = models.CharField(u'Previous School', max_length=50, blank=True, null=True, default="")
    qDueSubjects = models.IntegerField(u'Due Subjects', blank=True, null=True, default="")
    isActive = models.BooleanField(u'Active Registration', default=True, blank=True)
    student = models.ForeignKey('Student', related_name='ownerregistration')

class Imagen (models.Model):

    photo = models.FileField(u'Photo', upload_to="photos/", default='null')

    def __str__(self):
        #return "<a href='/photos/{}'>{}</a>".format(self.photo, self.photo)
        return  "<img src='/photos/{}' style='width:100px; height:100px;'/>".format(self.photo)
        #<img id='alum' src="{% static 'images/up.jpg' %}" alt='Foto alumno' style='width:200px; height:240px;margin-left:3%;'/>

    #def get_nombre(self):
    #   try:
    #        name = "photos/{}-{}-{}".format(self.nameStudent,self.lastNameStudent,self.dniStudent)
    #        alum = Registration.objects.filter(nameStudent = name)
    #        if img.count()>0:
    #            return img.first()
    #    except Exception as e:
    #        return None

