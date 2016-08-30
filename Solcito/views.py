from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from Solcito.models import Imagen, Student, Registration, Tutor
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Solcito.forms import EditRegistrationForm
from django.template.loader import render_to_string
import logging
#PDF
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

from .forms import StudentForm, GuardianForm

logger = logging.getLogger('django')

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

@require_GET
def index(request):
    context = RequestContext(request)
    student = Student()
    father = Tutor()
    mother = Tutor()
    tutor = Tutor()
    context['student_form']= StudentForm(instance = student)
    context['father_form']= GuardianForm(instance = father, prefix="father")
    context['mother_form']= GuardianForm(instance = mother, prefix="mother")
    context['guardian_form']= GuardianForm(instance = tutor, prefix="tutor")
    return render_to_response('matricular.html',{},context)


def editMatricula(request):

    student = Student()
    args = {}
    context = RequestContext(request)

    if request.method == 'POST':
        print "SI ES UN METODO POST"
        form = EditRegistrationForm(request.POST, request.FILES,
                instance=student)

        if form.is_valid():
            logger.info(form.instance)
            form.save()
    else:
        form = EditRegistrationForm(instance=student)
    args['form'] = form
    #return render(request, 'edit_matricula.html', args)
    return render(request, 'matricular.html', args)

def getFilter(request):
    context = RequestContext(request)
    return render_to_response('buscador.html',{},context)

#sex = (
#
#@login_required(login_url='/login/')
#def search(request):
#    context = RequestContext(request)
#    if request.method=='GET'
#        nombreA=request.GET['nombre']
#        apellidoA=request.GET['apellido']
#        dniA=request.GET['dni']
#        especialidadA=request.GET['especialidad']
#        cursoA=request.GET['curso']
#        matriculaA=request.GET['matricula']
#        legajoA = request.GET['legajo']
#        nombreM=request.GET['nombreMadre']
#        apellidoM=request.GET['apellidoMadre']
#        nombreP=request.GET['nombrePadre']
#        apellidoP=request.GET['apellidoPadre']
#        active=request.GET['activo']
#        matriculas = Registration.objects.all()
#        # Vamos filtrando por cada campo que el usuario completo
#        if nombreA != "":
#            matriculas = matriculas.filter(nameStudent__iexact=nombreA)
#            #print matriculas
#        if apellidoA != "":
#            matriculas = matriculas.filter(lastNameStudent__iexact=apellidoA)
#            #print matriculas
#        if dniA != "":
#            matriculas = matriculas.filter(dniStudent__iexact=dniA)
#            #print matriculas
#        if especialidadA != "":
#            matriculas = matriculas.filter(division__iexact=especialidadA)
#            #print matriculas
#        if cursoA != "":
#            matriculas = matriculas.filter(grade__iexact=cursoA)
#            #print matriculas
#        if matriculaA != "":
#            matriculas = matriculas.filter(administrativeFile__iexact=matriculaA)
#            #print matriculas
#        if legajoA != "":
#            matriculas = matriculas.filter(studentFile__iexact=legajoA)
#            #print matriculas
#        if nombreM != "":
#            matriculas = matriculas.filter(nameMother__iexact=nombreM)
#            #print matriculas
#        if apellidoM != "":
#            matriculas = matriculas.filter(lastNameMother__iexact=apellidoM)
#            #print matriculas
#        if nombreP != "":
#            matriculas = matriculas.filter(nameFather__iexact=nombreP)
#            #print matriculas
#        if apellidoP != "":
#            matriculas = matriculas.filter(lastNameFather__iexact=apellidoP)
#            #print matriculas
#        #De todas las matriculas del alumno muestra la activa
#        if active == "true":
#            matriculas = matriculas.filter(isActive=active)
#        return render_to_response('lista_buscador.html',{'matriculas':matriculas},context)
#
#
#https://github.com/eliluminado/esCUITValida/blob/master/esCUITValida.py
@require_POST
def confirmMatricula(request):
    context = RequestContext(request)

    sf = StudentForm(request.POST)
    ff= GuardianForm(request.POST, prefix='father')
    mf= GuardianForm(request.POST, prefix='mother')
    gf= GuardianForm(request.POST, prefix='tutor')

    if (sf.is_valid()):
        print "SUCCESS WITH STUDENT"
        if (ff.is_valid() or mf.is_valid() or gf.is_valid()):
            print "SUCCESS WITH TUTORS"
            context['valid'] = "true"
        else:
            context['valid'] = "false"
            print "ERRORSS!!!!!"
            print (ff.errors)
            print (mf.errors)
            print (gf.errors)
    else:
        context['valid'] = "false"
        print (sf.errors)

    diccionario = dict(request.POST)
    for element in diccionario:
        if "father" in element:
            diccionario[element.replace("father-", "f")] = diccionario.pop(element)
        if "mother" in element:
            diccionario[element.replace("mother-", "m")] = diccionario.pop(element)
        if "tutor" in element:
            diccionario[element.replace("tutor-", "g")] = diccionario.pop(element)


    context['student_form']= sf
    context['father_form']= ff
    context['mother_form']= mf
    context['guardian_form']= gf
    return render_to_response('matricular.html',{'data':diccionario},context)

def submitMatricula(request):
    context = RequestContext(request)
    if request.method=='POST':
        try:
            si = Student.objects.get(dni=request.POST['dni'])
        except:
            si = Student()
        try:
            fi = Tutor.objects.get(dni=request.POST['father-dni'])
        except:
            fi = Tutor(rol=1)
        try:
            mi = Tutor.objects.get(dni=request.POST['mother-dni'])
        except:
            mi = Tutor(rol=2)
        try:
            ti = Tutor.objects.get(dni=request.POST['tutor-dni'])
        except:
            ti = Tutor(rol=3)
        sf = StudentForm(request.POST, instance=si)
        ff= GuardianForm(request.POST, instance=fi, prefix='father')
        mf= GuardianForm(request.POST, instance=mi, prefix='mother')
        gf= GuardianForm(request.POST, instance=ti, prefix='tutor')
        if (sf.is_valid() ):
            sf.save()
            if ff.is_valid():
                ff.save()
            if mf.is_valid():
                mf.save()
            if gf.is_valid():
                gf.save()

            return render_to_response('matricula_success.html',{},context)

        else:
            print ("ERRORES!!!")
            print (sf.errors)

            context['student_form']= sf
            context['father_form']= ff
            context['mother_form']= mf
            context['tutor_form']= gf
            return render_to_response('matricular.html',{},context)

        #return render_to_response('matricula_success.html',{},context)
    return render_to_response('matricular_bug.html',{},context)

def html2pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    print "render"

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),
            content_type='application/pdf')
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
