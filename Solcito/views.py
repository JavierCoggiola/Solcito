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

from .forms import StudentForm, GuardianForm, PhotoForm

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
    photo = Imagen()
    context['student_form']= StudentForm(instance = student)
    context['father_form']= GuardianForm(instance = father, prefix="father")
    context['mother_form']= GuardianForm(instance = mother, prefix="mother")
    context['guardian_form']= GuardianForm(instance = tutor, prefix="guardian")
    context['photo_form']= PhotoForm(instance = photo, prefix="photo")
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
#    if request.method=='GET':
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
@require_POST
def confirmMatricula(request):
    context = RequestContext(request)
    context['ninguno'] = True

    '''try:
        si = Student.objects.get(dni=request.POST['dni'])
    except:
        si = Student(preinscipt_status=0)'''

    sf = StudentForm(request.POST)
    if (sf.is_valid()):
        sf.save()
        rendered = render_to_string('gracias_mail.html')
    else:
        print ("Errorsito")
        print (sf.errors)

        context['student_form']=sf
        return render_to_response('matricular.html',context)
    return redirect('/')

    pf = PhotoForm(request.POST)
    if (pf.is_valid()):
        pf.save()
        rendered = render_to_string('gracias_mail.html')
    else:
        print ("Error al cargar foto")
        print (pf.errors)

        context['photo_form']=pf
        return render_to_response('matricular.html',context)
    return redirect('/')

    #Ulises me dijo que no le de bola chamaco
    diccionario = dict(request.POST)
    for element in diccionario:
        if "father" in element:
            diccionario[element.replace("father-", "f")] = diccionario.pop(element)
        if "mother" in element:
            diccionario[element.replace("mother-", "m")] = diccionario.pop(element)
        if "guardian" in element:
            diccionario[element.replace("guardian-", "g")] = diccionario.pop(element)
        
    return render_to_response('dismatricula.html',{'data':diccionario},context)

def submitMatricula(request):
    context = RequestContext(request)
    if request.method=='POST':
        #print "POST"

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
