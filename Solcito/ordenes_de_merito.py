from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Solcito.models import OrdenDeMerito, Curso, RegistrationS, Student

def oredenes_de_merito(request):
    context = RequestContext(request)
    if request.user.groups.filter(name='Administrador').exists():
        return render_to_response('ordenes_de_merito.html', {'ordenes': OrdenDeMerito.objects.all(),'cursos':Curso.objects.all()}, context)
    else:
        return redirect('/admin')


    
def crear_orden_de_merito(request):
    mts = []
    als = []
    orden = request.GET['orden']
    cursos= request.GET['cursos']
    for a in cursos:
        mts = list(RegistrationS.objects.filter(curso = a))
        for mat in mts:
            if mat.student not in als:
                als.append(mat.student)