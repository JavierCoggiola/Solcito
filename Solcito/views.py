from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from Solcito.models import Student
# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('matricular.html',{},context)
def submitMatricula(request):
    context = RequestContext(request)
    if request.method=='POST':
        print "POST"
        alumno_nombre=request.POST['nombre']
        alumno_apellido=request.POST['apellido']
        alumno_dni=request.POST['dni']
        alumno_religion=request.POST['religion']
        alumno_sexo=request.POST['sexo']
        alumno_nacimiento=request.POST['nacimiento']
        alumno_lugar_nacimiento = request.POST['lugar_nacimiento']
        alumno_nacionalidad=request.POST['nacionalidad']
        alumno_calle=request.POST['calle']
        alumno_altura=request.POST['altura']
        alumno_barrio=request.POST['barrio']
        alumno_torre=request.POST['torre']
        alumno_piso=request.POST['piso']
        alumno_departamento=request.POST['departamento']
        alumno_postal=request.POST['postal']
        alumno_localidad=request.POST['localidad']
        alumno_mail=request.POST['mail']
        alumno_fijo=request.POST['fijo']
        alumno_celular=request.POST['celular']
        alumno = Student()
        alumno.name = alumno_nombre
        alumno.lastName = alumno_apellido
        alumno.dni = int(alumno_dni)
        alumno.sex = alumno_sexo
        alumno.religion = alumno_religion
        alumno.birthDate = alumno_nacimiento
        alumno.birthPlace = alumno_lugar_nacimiento
        alumno.nacionality = alumno_nacionalidad
        alumno.street = alumno_calle
        alumno.numberStreet = int(alumno_altura)
        alumno.neighborhood = alumno_barrio
        alumno.tower = alumno_torre
        print alumno_torre
        if alumno_piso != "":
            alumno.floorDepartment = int(alumno_piso)
            print alumno_piso
        alumno.department = alumno_departamento
        alumno.PC = int(alumno_postal)
        alumno.nacionality = alumno_nacionalidad
        alumno.email = alumno_mail
        alumno.landline = int(alumno_fijo)
        if alumno_celular != "":
            alumno.cellphone = int(alumno_celular)
        alumno.save()
        return render_to_response('matricular_success.html',{},context)
