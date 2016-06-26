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
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        dni=request.POST['dni']
        religion=request.POST['religion']
        sexo=request.POST['sexo']
        nacimiento=request.POST['nacimiento']
        lugar_nacimiento = request.POST['lugar_nacimiento']
        nacionalidad=request.POST['nacionalidad']
        calle=request.POST['calle']
        altura=request.POST['altura']
        barrio=request.POST['barrio']
        torre=request.POST['torre']
        piso=request.POST['piso']
        departamento=request.POST['departamento']
        postal=request.POST['postal']
        localidad=request.POST['localidad']
        mail=request.POST['mail']
        fijo=request.POST['fijo']
        celular=request.POST['celular']
        alumno = Student()
        alumno.name = nombre
        alumno.lastName = apellido
        alumno.dni = int(dni)
        alumno.sex = sexo
        alumno.religion = religion
        alumno.birthDate = nacimiento
        alumno.birthPlace = lugar_nacimiento
        alumno.nacionality = nacionalidad
        alumno.street = calle
        alumno.numberStreet = int(altura)
        alumno.neighborhood = barrio
        alumno.tower = torre
        print torre
        if piso != "":
            alumno.floorDepartment = int(piso)
            print piso
        alumno.department = departamento
        alumno.PC = int(postal)
        alumno.nacionality = nacionalidad
        alumno.email = mail
        alumno.landline = int(fijo)
        if celular != "":
            alumno.cellphone = int(celular)
        alumno.save()
        return render_to_response('matricular_success.html',{},context)
