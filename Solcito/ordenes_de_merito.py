from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Solcito.models import OrdenDeMerito, Curso

def oredenes_de_merito(request):
    context = RequestContext(request)
    if request.user.groups.filter(name='Administrador').exists():
        anos = []
        anos = list(set([curso.cycle for curso in Curso.objects.all()]))
        return render_to_response('ordenes_de_merito.html', {'ordenes': OrdenDeMerito.objects.all(),
                                                             'cursos':Curso.objects.all(),
                                                             'anos': anos}, context)
    else:
        return redirect('/admin')

