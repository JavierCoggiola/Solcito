from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Solcito.models import Imagen, Student, Registration
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#PDF
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def logMeIn(request): #Logueo
    context = RequestContext(request)
    errors = []
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user) #logueo de usuario por defecto de django
                return redirect('/solcito')
        else:
            errors.append(u"El usuario o la contrasena son incorrectos")
    return render_to_response('login.html',
                              {'errors':errors},
                              context)

def subirPhoto(request):
    context = RequestContext(request)
    max_upload_size = 5242880

    if request.method=='POST':
        student=Imagen()
        student.photo=request.FILES['photo']

        nombre=request.POST.get("nombre")
        apellido=request.POST.get("apellido")
        dni=request.POST.get('dni')

        spliting = student.photo.name.split(".")
        extension = spliting[len(spliting)-1]
        student.photo.name = nombre+"-"+apellido+"-"+dni+"."+extension

        if student.photo.size > max_upload_size:
            print ("archivo pesado")
            return render_to_response('matricular_foto.html',{},context)
        else:
            print ("guardado de alumno correcto")
            student.save()

        return HttpResponse(status=200)
    return render_to_response('matricular.html',
context)

def logMeOut(request):
    logout(request) #Logout de django
    context = RequestContext(request)
    return redirect('/')

def index(request):
    context = RequestContext(request)
    return render_to_response('matricular.html',{},context)

def editMatricula(request):
    context = RequestContext(request)
    
    if request.method=='GET':
        matid=request.GET['idMatricula']
        matricula = Registration.objects.get(pk=matid)
        return render_to_response('profile.html',{'matricula':matricula},context)
    if request.method=='POST':
        #print "POST"
        matid=request.POST['idmat']
        mat_numero_legajo=request.POST['numleg']
        mat_legajo_administrativo=request.POST['legadm']
        mat_ano_to_mat=request.POST['anotomat']
        mat_div_to_mat=request.POST['divtomat']
        mat_prev_school=request.POST['prschool']
        mat_q_due_mat=request.POST['qduemat']
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
                #print i.nameStudent
                i.isActive = True
                i.save()
            #print "Alumno Existe"
        except ObjectDoesNotExist:
            #print "Alumno NO Existe"
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
            #print alumno_torre
            if alumno_piso != "":
                alumno.floorDepartment = int(alumno_piso)
                #print alumno_piso
            alumno.department = alumno_departamento
            alumno.PC = int(alumno_postal)
            alumno.nacionality = alumno_nacionalidad
            alumno.email = alumno_mail
            alumno.landline = int(alumno_fijo)
            if alumno_celular != "":
                alumno.cellphone = int(alumno_celular)
            alumno.save()

        alumno = Student.objects.get(dni=int(alumno_dni))
        matricula = Registration.objects.get(pk=matid)

        matricula.studentFile = int(mat_numero_legajo)
        matricula.administrativeFile = int(mat_legajo_administrativo)
        matricula.grade = int(mat_ano_to_mat)
        matricula.division = mat_div_to_mat
        matricula.previousSchool = mat_prev_school
        matricula.qDueSubjects = int(mat_q_due_mat)

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
            #print alumno_piso
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
            
        matriculas = Registration.objects.filter(student=alumno)
        for i in matriculas:
            #print i.nameStudent
            i = matricula
            i.save()
                
        return redirect('/solcito')
    return render_to_response('matricular_bug.html',{},context)

def getFilter(request):
    context = RequestContext(request)
    return render_to_response('buscador.html',{},context)

@login_required(login_url='/login/')
def search(request):
    context = RequestContext(request)
    if request.method=='GET':
        nombreA=request.GET['nombre']
        apellidoA=request.GET['apellido']
        dniA=request.GET['dni']
        especialidadA=request.GET['especialidad']
        cursoA=request.GET['curso']
        matriculaA=request.GET['matricula']
        legajoA = request.GET['legajo']
        nombreM=request.GET['nombreMadre']
        apellidoM=request.GET['apellidoMadre']
        nombreP=request.GET['nombrePadre']
        apellidoP=request.GET['apellidoPadre']
        active=request.GET['activo']
        matriculas = Registration.objects.all()
        # Vamos filtrando por cada campo que el usuario completo
        if nombreA != "":
            matriculas = matriculas.filter(nameStudent__iexact=nombreA)
            #print matriculas
        if apellidoA != "":
            matriculas = matriculas.filter(lastNameStudent__iexact=apellidoA)
            #print matriculas
        if dniA != "":
            matriculas = matriculas.filter(dniStudent__iexact=dniA)
            #print matriculas
        if especialidadA != "":
            matriculas = matriculas.filter(division__iexact=especialidadA)
            #print matriculas
        if cursoA != "":
            matriculas = matriculas.filter(grade__iexact=cursoA)
            #print matriculas
        if matriculaA != "":
            matriculas = matriculas.filter(administrativeFile__iexact=matriculaA)
            #print matriculas
        if legajoA != "":
            matriculas = matriculas.filter(studentFile__iexact=legajoA)
            #print matriculas
        if nombreM != "":
            matriculas = matriculas.filter(nameMother__iexact=nombreM)
            #print matriculas
        if apellidoM != "":
            matriculas = matriculas.filter(lastNameMother__iexact=apellidoM)
            #print matriculas
        if nombreP != "":
            matriculas = matriculas.filter(nameFather__iexact=nombreP)
            #print matriculas
        if apellidoP != "":
            matriculas = matriculas.filter(lastNameFather__iexact=apellidoP)
            #print matriculas
        #De todas las matriculas del alumno muestra la activa
        if active == "true":
            matriculas = matriculas.filter(isActive=active)
        return render_to_response('lista_buscador.html',{'matriculas':matriculas},context)


def confirmMatricula(request):
    context = RequestContext(request)
    print "confirmado"
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
    data= {
        #Datos Alumno
        'alumnoNombre': alumno_nombre,
        'alumnoApellido': alumno_apellido,
        'alumnoDni': alumno_dni,
        'alumnoReligion': alumno_religion,
        'alumnoSexo': alumno_sexo,
        'alumnoNacimiento': alumno_nacimiento,
        'alumnoLugarNacimiento': alumno_lugar_nacimiento,
        'alumnoNacionalidad': alumno_nacionalidad,
        'alumnoCalle': alumno_calle,
        'alumnoAltura': alumno_altura,
        'alumnoBarrio': alumno_barrio,
        'alumnoTorre': alumno_torre,
        'alumnoPiso': alumno_piso,
        'alumnoDepartamento': alumno_departamento,
        'alumnoPostal': alumno_postal,
        'alumnoLocalidad': alumno_localidad,
        'alumnoMail': alumno_mail,
        'alumnoFijo': alumno_fijo,
        'alumnoCel': alumno_celular,
        #Datos Padre
        'padreNombre': padre_nombre,
        'padreApellido': padre_apellido,
        'padreDni': padre_dni,
        'padreCuil': padre_cuil,
        'padreTrabajo': padre_trabajo,
        'padreProfesion': padre_profesion,
        'padreNacionalidad': padre_nacionalidad,
        'padreCalle': padre_calle,
        'padreAltura': padre_altura,
        'padreBarrio': padre_barrio,
        'padreTorre': padre_torre,
        'padrePiso': padre_piso,
        'padreDepartamento': padre_departamento,
        'padrePostal': padre_postal,
        'padreLocalidad': padre_localidad,
        'padreMail': padre_mail,
        'padreFijo': padre_fijo,
        'padreCel': padre_celular,
        'padreLaboral': padre_tlaboral,
        #Datos Madre
        'madreNombre':madre_nombre,
        'madreApellido':madre_apellido,
        'madreDni':madre_dni,
        'madreCuil':madre_cuil,
        'madreTrabajo':madre_trabajo,
        'madreProfesion':madre_profesion,
        'madreNacionalidad':madre_nacionalidad,
        'madreCalle':madre_calle,
        'madreAltura':madre_altura,
        'madreBarrio':madre_barrio,
        'madreTorre':madre_torre,
        'madrePiso':madre_piso,
        'madreDepartamento':madre_departamento,
        'madrePosta':madre_postal,
        'madreLocalidad':madre_localidad,
        'madreMail':madre_mail,
        'madreFijo':madre_fijo,
        'madreCel':madre_celular,
        'madreLaboral':madre_tlaboral,
        #Datos Tutor
        'tutorNombre':tutor_nombre,
        'tutorApellido':tutor_apellido,
        'tutorDni':tutor_dni,
        'tutorCuil':tutor_cuil,
        'tutorTrabajo':tutor_trabajo,
        'tutorProfesion':tutor_profesion,
        'tutorNacionalidad':tutor_nacionalidad,
        'tutorCalle':tutor_calle,
        'tutorAltura':tutor_altura,
        'tutorBarrio':tutor_barrio,
        'tutorTorre':tutor_torre,
        'tutorPiso':tutor_piso,
        'tutorDepartamento':tutor_departamento,
        'tutorPostal':tutor_postal,
        'tutorLocalidad':tutor_localidad,
        'tutorMail':tutor_mail,
        'tutorFijo':tutor_fijo,
        'tutorCel':tutor_celular,
        'tutorLaboral':tutor_tlaboral,
    }
    return render_to_response('dismatricula.html',{'data':data},context)

def submitMatricula(request):
    context = RequestContext(request)
    if request.method=='POST':
        #print "POST"
        alumno_nombre=request.POST['nombre']
        print alumno_nombre
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
                #print (i.nameStudent)
                i.isActive = False
                i.save()
            #print ("Alumno Existe")
        except ObjectDoesNotExist:
            #print ("Alumno NO Existe")
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
            #print (alumno_torre)
            if alumno_piso != "":
                alumno.floorDepartment = int(alumno_piso)
                #print (alumno_piso)
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
            #print (alumno_piso)
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
            matricula.cellphoneTutor = int(tutor_celular)
        if tutor_tlaboral != "":
            matricula.workPhoneTutor = int(tutor_tlaboral)

        matricula.save()
        idMat = matricula.idRegistration
        return HttpResponse( idMat)
        #return render_to_response('matricula_success.html',{},context)
    return render_to_response('matricular_bug.html',{},context)

def html2pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    filename = 'somefilename.pdf'
    print "render"

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result, filename)
    if not pdf.err:
        return HttpResponse(result.getvalue(),
            content_type='application/pdf')

#CON ESTE CODIGO SE CAMBIA EL ARCHVIO DEL PDF DESCARGADO AUTOMATICAMENTE, PERO SE PIERDE EL PDF PREVIEW.
        """response = HttpResponse(result.getvalue(), 
            content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=Client_Summary.pdf'
        return response"""

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def genpdf(request,id_matricula):
    print id_matricula
    registration = Registration.objects.get(pk=id_matricula)
    #Retrieve data or whatever you need
    return html2pdf(
        'pdf.html',
        {
            'pagesize':'A4',
            'matricula':registration
        }
    )
    print "return"

def profile(request):
    context = RequestContext(request)
    return render_to_response('profile.html',{},context)