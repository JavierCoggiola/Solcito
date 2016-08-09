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
    name = models.CharField(u'Name', max_length=50, blank=False)
    lastName = models.CharField(u'Last Name', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    sex = models.CharField(u'Sex', max_length=1, choices=sex, default='M', blank=False)
    religion = models.CharField(u'Religion', max_length=3, choices=religion, default='cat', blank=False)
    birthDate = models.DateField(u'Birth Date', blank=False)
    birthPlace = models.CharField(u'Birth Place', max_length=50, blank=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, blank=False)
    street = models.CharField(u'Street', max_length=50, blank=False)
    numberStreet = models.IntegerField(u'Number Street', blank=False)
    neighborhood = models.CharField(u'Neighborhood', max_length=50, blank=False)
    tower = models.CharField(u'Tower', max_length=20, blank=True, null=True, default="")
    floorDepartment = models.IntegerField(u'Department Floor', blank=True, null=True, default="")
    department = models.CharField(u'Department', max_length=20, blank=True, null=True, default="")
    PC = models.IntegerField(u'Postal Code', blank=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    landline = models.IntegerField(u'Landline', blank=False)
    cellphone = models.IntegerField(u'Cellphone', blank=True, null=True, default="")

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
    
    def __str__(self):
        return self.name
    
class Tutor (models.Model):

    idTutor = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Name', max_length=50, blank=False)
    lastName = models.CharField(u'Last Name', max_length=50, blank=False)
    dni = models.IntegerField(u'DNI', blank=False)
    cuil = models.IntegerField(u'Cuil', blank=False)
    rol = models.IntegerField(u'Rol', max_length=3, choices=rol, default='fat', blank=False)
    workPlace = models.CharField(u'Work Place', max_length=50, blank=False)
    profession = models.CharField(u'Profession', max_length=50, blank=False)
    locality = models.CharField(u'Locality', max_length=50, default="", blank=False)
    street = models.CharField(u'Street', max_length=50, blank=False)
    numberStreet = models.IntegerField(u'Number Street', blank=False)
    neighborhood = models.CharField(u'Neighborhood', max_length=50, blank=False)
    tower = models.CharField(u'Tower', max_length=20, blank=True, null=True)
    floorDepartment = models.IntegerField(u'Department Floor', blank=True, null=True)
    department = models.CharField(u'Department', max_length=20, blank=True, null=True)
    PC = models.IntegerField(u'Postal Code', blank=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, blank=False)
    email = models.CharField(u'Email', max_length=50, blank=False)
    landline = models.IntegerField(u'Landline', blank=False)
    cellphone = models.IntegerField(u'Cellphone', blank=True, null=True)
    workPhone = models.IntegerField(u'Work Phone', blank=True, null=True)

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
    
    nameStudent = models.CharField(u'Name Student', max_length=50, blank=False, null=True)
    lastNameStudent = models.CharField(u'Last Name Student', max_length=50, blank=False, null=True)
    dniStudent = models.IntegerField(u'DNI Student', blank=False, null=True)
    sexStudent = models.CharField(u'Sex Student', max_length=1, choices=sex, default='M', blank=False, null=True)
    religionStudent = models.CharField(u'Religion Student', max_length=50, blank=False, null=True)
    birthDateStudent = models.DateField(u'Birth Date Student', blank=False, null=True)
    birthPlaceStudent = models.CharField(u'Birth Place Student', max_length=50, blank=False, null=True)
    localityStudent = models.CharField(u'Locality Student', max_length=50, blank=False, null=True)
    nacionalityStudent = models.CharField(u'Nacionality Student', max_length=50, blank=False, null=True)
    streetStudent = models.CharField(u'Street Student', max_length=50, blank=False, null=True)
    numberStreetStudent = models.IntegerField(u'Number Street Student', blank=False, null=True)
    neighborhoodStudent = models.CharField(u'Neighborhood Student', max_length=50, blank=False, null=True)
    towerStudent = models.CharField(u'Tower Student', max_length=20, blank=True, null=True)
    floorDepartmentStudent = models.IntegerField(u'Department Floor Student', blank=True, null=True)
    departmentStudent = models.CharField(u'Department Student', max_length=20, blank=True, null=True)
    PCStudent = models.IntegerField(u'Postal Code Student', blank=False, null=True)
    nacionalityStudent = models.CharField(u'Nacionality Student', max_length=50, blank=False, null=True)
    emailStudent = models.CharField(u'Email Student', max_length=50, blank=False, null=True)
    landlineStudent = models.IntegerField(u'Landline Student', blank=False, null=True)
    cellphoneStudent = models.IntegerField(u'Cellphone Student', blank=True, null=True)

    nameFather = models.CharField(u'Name Father', max_length=50, blank=True, null=True)
    lastNameFather = models.CharField(u'Last Name Father', max_length=50, blank=True, null=True)
    dniFather = models.IntegerField(u'DNI Father', blank=True, null=True)
    cuilFather = models.IntegerField(u'Cuil Father', blank=True, null=True)
    workPlaceFather = models.CharField(u'Work Place Father', max_length=50, blank=True, null=True)
    professionFather = models.CharField(u'Profession Father', max_length=50, blank=True, null=True)
    localityFather = models.CharField(u'Locality Father', max_length=50, default="", blank=True, null=True)
    streetFather = models.CharField(u'Street Father', max_length=50, blank=True, null=True)
    numberStreetFather = models.IntegerField(u'Number Street Father', blank=True, null=True)
    neighborhoodFather = models.CharField(u'Neighborhood Father', max_length=50, blank=True, null=True)
    towerFather = models.CharField(u'Tower Father', max_length=20, blank=True, null=True)
    floorDepartmentFather = models.IntegerField(u'Department Floor Father', blank=True, null=True)
    departmentFather = models.CharField(u'Department Father', max_length=20, blank=True, null=True)
    PCFather = models.IntegerField(u'Postal Code  Father', blank=True, null=True)
    nacionalityFather = models.CharField(u'Nacionality Father', max_length=50, blank=True, null=True)
    emailFather = models.CharField(u'Email Father', max_length=50, blank=True, null=True)
    landlineFather = models.IntegerField(u'Landline Father', blank=True, null=True)
    cellphoneFather = models.IntegerField(u'Cellphone Father', blank=True, null=True)
    workPhoneFather = models.IntegerField(u'Work Phone Father', blank=True, null=True)

    nameMother = models.CharField(u'Name Mother', max_length=50, blank=True, null=True)
    lastNameMother = models.CharField(u'Last Name Mother', max_length=50, blank=True, null=True)
    dniMother = models.IntegerField(u'DNI Mother', blank=True, null=True)
    cuilMother = models.IntegerField(u'Cuil Mother', blank=True, null=True)
    workPlaceMother = models.CharField(u'Work Place Mother', max_length=50, blank=True, null=True)
    professionMother = models.CharField(u'Profession Mother', max_length=50, blank=True, null=True)
    localityMother = models.CharField(u'Locality Mother', max_length=50, default="", blank=True, null=True)
    streetMother = models.CharField(u'Street Mother', max_length=50, blank=True, null=True)
    numberStreetMother = models.IntegerField(u'Number Street Mother', blank=True, null=True)
    neighborhoodMother = models.CharField(u'Neighborhood Mother', max_length=50, blank=True, null=True)
    towerMother = models.CharField(u'Tower Mother', max_length=20, blank=True, null=True)
    floorDepartmentMother = models.IntegerField(u'Department Floor Mother', blank=True, null=True)
    departmentMother = models.CharField(u'Department Mother', max_length=20, blank=True, null=True)
    PCMother = models.IntegerField(u'Postal Code Mother', blank=True, null=True)
    nacionalityMother = models.CharField(u'Nacionality Mother', max_length=50, blank=True, null=True)
    emailMother = models.CharField(u'Email Mother', max_length=50, blank=True, null=True)
    landlineMother = models.IntegerField(u'Landline Mother', blank=True, null=True)
    cellphoneMother = models.IntegerField(u'Cellphone Mother', blank=True, null=True)
    workPhoneMother = models.IntegerField(u'Work Phone Mother', blank=True, null=True)

    nameTutor = models.CharField(u'Name Tutor', max_length=50, blank=True, null=True)
    lastNameTutor = models.CharField(u'Last Name Tutor', max_length=50, blank=True, null=True)
    dniTutor = models.IntegerField(u'DNI Tutor', blank=True, null=True)
    cuilTutor = models.IntegerField(u'Cuil Tutor', blank=True, null=True)
    workPlaceTutor = models.CharField(u'Work Place Tutor', max_length=50, blank=True, null=True)
    professionTutor = models.CharField(u'Profession Tutor', max_length=50, blank=True, null=True)
    localityTutor = models.CharField(u'Locality Tutor', max_length=50, default="", blank=True, null=True)
    streetTutor = models.CharField(u'Street Tutor', max_length=50, blank=True, null=True)
    numberStreetTutor = models.IntegerField(u'Number Street Tutor', blank=True, null=True)
    neighborhoodTutor = models.CharField(u'Neighborhood Tutor', max_length=50, blank=True, null=True)
    towerTutor = models.CharField(u'Tower Tutor', max_length=20, blank=True, null=True)
    floorDepartmentTutor = models.IntegerField(u'Department Floor Tutor', blank=True, null=True)
    departmentTutor = models.CharField(u'Department Tutor', max_length=20, blank=True, null=True)
    PCTutor = models.IntegerField(u'Postal Code Tutor', blank=True, null=True)
    nacionalityTutor = models.CharField(u'Nacionality Tutor', max_length=50, blank=True, null=True)
    emailTutor = models.CharField(u'Email Tutor', max_length=50, blank=True, null=True)
    landlineTutor = models.IntegerField(u'Landline Tutor', blank=True, null=True)
    cellphoneTutor = models.IntegerField(u'Cellphone Tutor', blank=True, null=True)
    workPhoneTutor = models.IntegerField(u'Work Phone Tutor', blank=True, null=True)



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

