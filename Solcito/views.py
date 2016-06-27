from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from Solcito.models import Imagen, Student, Registration
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def entrada(request):
    context = RequestContext(request)
    if request.method=='POST':


        img=Imagen()
        img.img=request.FILES[img]
        img.desc=request.POST[desc]
        img.save()
        return redirect("/")
    return render_to_response('matricular.html',
context)


def index(request):
    context = RequestContext(request)
    return render_to_response('matricular.html',{},context)

def submitMatricula(request):
    context = RequestContext(request)
    if request.method=='POST':
        #print "POST"
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
            matriculas = Registration.objects.filter(student=alumno)
            for i in matriculas:
                print i.nameStudent
                i.isActive = False
                i.save()
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

        alumno = Student.objects.get(dni=int(alumno_dni))
        matricula = Registration()

        matricula.student = alumno

        matricula.nameStudent = alumno_nombre
        matricula.lastNameStudent = alumno_apellido
        matricula.dniStudent = int(alumno_dni)
        matricula.sexStudent = alumno_sexo
        matricula.religionStudent = alumno_religion
        matricula.birthDateStudent = alumno_nacimiento
        matricula.birthPlaceStudent = alumno_lugar_nacimiento
        matricula.nacionalityStudent = alumno_nacionalidad
        matricula.streetStudent = alumno_calle
        matricula.numberStreetStudent = int(alumno_altura)
        matricula.neighborhoodStudent = alumno_barrio
        matricula.towerStudent = alumno_torre
        if alumno_piso != "":
            matricula.floorDepartmentStudent = int(alumno_piso)
            print alumno_piso
        matricula.departmentStudent = alumno_departamento
        matricula.PCStudent = int(alumno_postal)
        matricula.nacionalityStudent = alumno_nacionalidad
        matricula.emailStudent = alumno_mail
        matricula.landlineStudent = int(alumno_fijo)
        if alumno_celular != "":
            matricula.cellphoneStudent = int(alumno_celular)

        matricula.nameMother = madre_nombre
        matricula.lastNameMother = madre_apellido
        if madre_dni != "":
            matricula.dniMother = int(madre_dni)
        if madre_cuil != "":
            matricula.cuilMother = int(madre_cuil)
        matricula.workPlaceMother = madre_trabajo
        matricula.professionMother = madre_profesion
        matricula.nacionalityMother = madre_nacionalidad
        matricula.streetMother = madre_calle
        if madre_altura != "":
            matricula.numberStreetMother = int(madre_altura)
        matricula.neighborhoodMother = madre_barrio
        matricula.towerMother = madre_torre
        if madre_piso != "":
            matricula.floorDepartmentMother = int(madre_piso)
        matricula.departmentMother = madre_departamento
        if madre_postal != "":
            matricula.PCMother = int(madre_postal)
        matricula.localityMother = madre_localidad
        matricula.emailMother = madre_mail
        if madre_fijo != "":
            matricula.landlineMother = int(madre_fijo)
        if madre_celular != "":
            matricula.cellphoneMother = int(madre_celular)
        if madre_tlaboral != "":
            matricula.workPhoneMother = int(madre_tlaboral)


        #student (decir a que estudiante corresponde el tutor)



        matricula.nameFather = padre_nombre
        matricula.lastNameFather = padre_apellido
        if padre_dni != "":
            matricula.dniFather = int(padre_dni)
        if padre_cuil != "":
            matricula.cuilFather = int(padre_cuil)
        matricula.workPlaceFather = padre_trabajo
        matricula.professionFather = padre_profesion
        matricula.nacionalityFather = padre_nacionalidad
        matricula.streetFather = padre_calle
        if padre_altura != "":
            matricula.numberStreetFather = int(padre_altura)
        matricula.neighborhoodFather = padre_barrio
        matricula.towerFather = padre_torre
        if padre_piso != "":
            matricula.floorDepartmentFather = int(padre_piso)
        matricula.departmentFather = padre_departamento
        if padre_postal != "":
            matricula.PCFather = int(padre_postal)
        matricula.localityFather = padre_localidad
        matricula.emailFather = padre_mail
        if padre_fijo != "":
            matricula.landlineFather = int(padre_fijo)
        if padre_celular != "":
            matricula.cellphoneFather = int(padre_celular)
        if padre_tlaboral != "":
            matricula.workPhoneFather = int(padre_tlaboral)


        #student (decir a que estudiante corresponde el tutor)



        matricula.nameTutor = tutor_nombre
        matricula.lastNameTutor = tutor_apellido
        if tutor_dni != "":
            matricula.dniTutor = int(tutor_dni)
        if tutor_cuil != "":
            matricula.cuilTutor = int(tutor_cuil)
        matricula.workPlaceTutor = tutor_trabajo
        matricula.professionTutor = tutor_profesion
        matricula.nacionalityTutor = tutor_nacionalidad
        matricula.streetTutor = tutor_calle
        if tutor_altura != "":
            matricula.numberStreetTutor = int(tutor_altura)
        matricula.neighborhoodTutor = tutor_barrio
        matricula.towerTutor = tutor_torre
        if tutor_piso != "":
            matricula.floorDepartmentTutor = int(tutor_piso)
        matricula.departmentTutor = tutor_departamento
        if tutor_postal != "":
            matricula.PCTutor = int(tutor_postal)
        matricula.localityTutor = tutor_localidad
        matricula.emailTutor = tutor_mail
        if tutor_fijo != "":
            matricula.landlineTutor = int(tutor_fijo)
        if tutor_celular != "":
            matriculaFather.cellphoneTutor = int(tutor_celular)
        if tutor_tlaboral != "":
            matricula.workPhoneTutor = int(tutor_tlaboral)

        matricula.save()



        return render_to_response('matricular_success.html',{},context)
    return render_to_response('matricular_bug.html',{},context)
