
from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from Solcito.models import Student, Registration, Tutor
# exepciones
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('matricular.html',{},context)

def search(request):
    context = RequestContext(request)
    return render_to_response('buscar.html',{},context)

def editMatricula(request, idReg):
    context = RequestContext(request)
    matricula = Registration.objects.get(pk='00001')
    return render_to_response('edit_matricula.html',{'matricula':matricula},context)

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
        madre_nombre=request.POST['nombrem']
        madre_apellido=request.POST['apellidom']
        madre_dni=request.POST['dnim']
        madre_cuil=request.POST['cuilm']
        madre_trabajo=request.POST['lugartrabajom']
        madre_profesion=request.POST['profesionm']
        madre_nacionalidad=request.POST['nacionalidadm']
        madre_calle=request.POST['callem']
        madre_altura=request.POST['alturam']
        madre_barrio=request.POST['barriom']
        madre_torre=request.POST['torrem']
        madre_piso=request.POST['pisom']
        madre_departamento=request.POST['departamentom']
        madre_postal=request.POST['postalm']
        madre_localidad=request.POST['localidadm']
        madre_mail=request.POST['mailm']
        madre_fijo=request.POST['fijom']
        madre_celular=request.POST['celularm']
        madre_tlaboral=request.POST['tlaboralm']
        padre_nombre=request.POST['nombrep']
        padre_apellido=request.POST['apellidop']
        padre_dni=request.POST['dnip']
        padre_cuil=request.POST['cuilp']
        padre_trabajo=request.POST['lugartrabajop']
        padre_profesion=request.POST['profesionp']
        padre_nacionalidad=request.POST['nacionalidadp']
        padre_calle=request.POST['callep']
        padre_altura=request.POST['alturap']
        padre_barrio=request.POST['barriop']
        padre_torre=request.POST['torrep']
        padre_piso=request.POST['pisop']
        padre_departamento=request.POST['departamentop']
        padre_postal=request.POST['postalp']
        padre_localidad=request.POST['localidadp']
        padre_mail=request.POST['mailp']
        padre_fijo=request.POST['fijop']
        padre_celular=request.POST['celularp']
        padre_tlaboral=request.POST['tlaboralp']
        tutor_nombre=request.POST['nombret']
        tutor_apellido=request.POST['apellidot']
        tutor_dni=request.POST['dnit']
        tutor_cuil=request.POST['cuilt']
        tutor_trabajo=request.POST['lugartrabajot']
        tutor_profesion=request.POST['profesiont']
        tutor_nacionalidad=request.POST['nacionalidadt']
        tutor_calle=request.POST['callet']
        tutor_altura=request.POST['alturat']
        tutor_barrio=request.POST['barriot']
        tutor_torre=request.POST['torret']
        tutor_piso=request.POST['pisot']
        tutor_departamento=request.POST['departamentot']
        tutor_postal=request.POST['postalt']
        tutor_localidad=request.POST['localidadt']
        tutor_mail=request.POST['mailt']
        tutor_fijo=request.POST['fijot']
        tutor_celular=request.POST['celulart']
        tutor_tlaboral=request.POST['tlaboralt']


        try:
            alumno = Student.objects.get(dni=int(alumno_dni))
            print "Alumno Existe"
        except ObjectDoesNotExist:
            print "Alumno NO Existe"
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

        madre = Tutor.rol= 1
        madre.name = madre_nombre
        madre.lastName = madre_apellido
        madre.dni = int(madre_dni)
        madre.cuil = int(madre_cuil)
        madre.workPlace = madre_trabajo
        madre.profession = madre_profesion
        madre.nacionality = madre_nacionalidad
        madre.street = madre_calle
        madre.numberStreet = madre_altura
        madre.neighborhood = madre_barrio
        madre.tower = madre_torre
        if madre_piso != "":
            madre.floorDepartment = int(madre_piso)
        madre.department = madre_departamento
        madre.PC = madre_postal
        madre.locality = madre_localidad
        madre.email = madre_mail
        madre.landline = madre_fijo
        if madre_celular != "":
            madre.cellphone = int(madre_celular)
        if madre_tlaboral != "":
            madre.workPhone = int(madre_tlaboral)
        madre.save()

        #student (decir a que estudiante corresponde el tutor)

        padre = Tutor.rol= 0
        padre.name = padre_nombre
        padre.lastName = padre_apellido
        padre.dni = int(padre_dni)
        padre.cuil = int(padre_cuil)
        padre.workPlace = padre_trabajo
        padre.profession = padre_profesion
        padre.nacionality = padre_nacionalidad
        padre.street = padre_calle
        padre.numberStreet = padre_altura
        padre.neighborhood = padre_barrio
        padre.tower = padre_torre
        if padre_piso != "":
            padre.floorDepartment = int(padre_piso)
        padre.department = padre_departamento
        padre.PC = padre_postal
        padre.locality = padre_localidad
        padre.email = padre_mail
        padre.landline = padre_fijo
        if padre_celular != "":
            padre.cellphone = int(padre_celular)
        if padre_tlaboral != "":
            padre.workPhone = int(padre_tlaboral)
        padre.save()

        #student (decir a que estudiante corresponde el tutor)

        tutor = Tutor.rol= 2
        tutor.name = tutor_nombre
        tutor.lastName = tutor_apellido
        tutor.dni = int(tutor_dni)
        tutor.cuil = int(tutor_cuil)
        tutor.workPlace = tutor_trabajo
        tutor.profession = tutor_profesion
        tutor.nacionality = tutor_nacionalidad
        tutor.street = tutor_calle
        tutor.numberStreet = tutor_altura
        tutor.neighborhood = tutor_barrio
        tutor.tower = tutor_torre
        if tutor_piso != "":
            tutor.floorDepartment = int(tutor_piso)
        tutor.department = tutor_departamento
        tutor.PC = tutor_postal
        tutor.locality = tutor_localidad
        tutor.email = tutor_mail
        tutor.landline = tutor_fijo
        if tutor_celular != "":
            tutor.cellphone = int(tutor_celular)
        if tutor_tlaboral != "":
            tutor.workPhone = int(tutor_tlaboral)
        tutor.save()

        #student (decir a que estudiante corresponde el tutor)

        return render_to_response('matricular_success.html',{},context)
    return render_to_response('matricular_bug.html',{},context)
