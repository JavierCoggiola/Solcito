from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

sex = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)

class Student(models.Model):
    idStudent = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Name', max_length=50, null=False)
    lastName = models.CharField(u'Last Name', max_length=50, null=False)
    dni = models.IntegerField(u'DNI', null=False)
    sex = models.CharField(u'Sex', max_length=1, choices=sex, default='M', null=False)
    religion = models.CharField(u'Religion', max_length=50, null=False)
    birthDate = models.DateField(u'Birth Date', null=False)
    birthPlace = models.CharField(u'Birth Place', max_length=50, null=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, null=False)
    street = models.CharField(u'Street', max_length=50, null=False)
    numberStreet = models.IntegerField(u'Number Street', null=False)
    neighborhood = models.CharField(u'Neighborhood', max_length=50, null=False)
    tower = models.CharField(u'Tower', max_length=20, null=True)
    floorDepartment = models.IntegerField(u'Department Floor', null=True)
    department = models.CharField(u'Department', max_length=20, null=True)
    PC = models.IntegerField(u'Postal Code', null=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, null=False)
    email = models.CharField(u'Email', max_length=50, null=False)
    landline = models.IntegerField(u'Landline', null=False)
    cellphone = models.IntegerField(u'Cellphone', null=True)
    photo = models.FileField(u'Photo', upload_to='photos/', null=True)

    def __str__(self):
		return self.name
    
class Registration(models.Model):
    idRegistration = models.AutoField(primary_key=True, editable=False)
    studentFile = models.IntegerField(u'Student File', null=False)
    administrativeFile = models.IntegerField(u'Administrative File', null=False)
    course = models.IntegerField(u'Course', null=False)
    division = models.CharField(u'Division', max_length=1, null=True)
    previousSchool = models.CharField(u'Previous School', max_length=50, null=True)
    qDueSubjects = models.IntegerField(u'Due Subjects', null=True)
    isActive = models.BooleanField(u'Active Registration', default=True, null=False)
    student = models.ForeignKey('Student', related_name='ownerregistration')
    
class Tutor (models.Model):
 
    FATHER = 0
    MOTHER = 1
    TUTOR = 2
    TUTOR_ROL = (
        (FATHER, "Father"),
        (MOTHER, "Mother"),
        (TUTOR, "Tutor"),
    )
    
    idTutor = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(u'Name', max_length=50, null=False)
    lastName = models.CharField(u'Last Name', max_length=50, null=False)
    dni = models.IntegerField(u'DNI', null=False)
    cuil = models.IntegerField(u'Cuil', null=False)
    rol = models.IntegerField(u'Rol', choices=TUTOR_ROL, default=TUTOR, null=False)
    workPlace = models.CharField(u'Work Place', max_length=50, null=False)
    profession = models.CharField(u'Profession', max_length=50, null=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, null=False)
    street = models.CharField(u'Street', max_length=50, null=False)
    numberStreet = models.IntegerField(u'Number Street', null=False)
    neighborhood = models.CharField(u'Neighborhood', max_length=50, null=False)
    tower = models.CharField(u'Tower', max_length=20, null=True)
    floorDepartment = models.IntegerField(u'Department Floor', null=True)
    department = models.CharField(u'Department', max_length=20, null=True)
    PC = models.IntegerField(u'Postal Code', null=False)
    nacionality = models.CharField(u'Nacionality', max_length=50, null=False)
    email = models.CharField(u'Email', max_length=50, null=False)
    landline = models.IntegerField(u'Landline', null=False)
    cellphone = models.IntegerField(u'Cellphone', null=True)
    workPhone = models.IntegerField(u'Work Phone', null=True)
    student = models.OneToOneField(Student, related_name='son')
