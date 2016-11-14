from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Solcito.models import OrdenDeMerito, Curso, Student

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


def ordenar(request):
    context = RequestContext(request)

    ord = request.GET.get('orden')

    cursos = Curso.objects.filter(pk__in=request.GET.getlist('cursos[]'))
    students = Student.objects.filter(ownerregistration__curso__in=list(cursos))
    result = []
    for student in students:
        stud = {}
        stud['name'] = student.name
        stud['apellido'] = student.lastName
        stud['puntaje'] = student.get_score(ord,cursos)
        result.append(stud)
    result.sort(key=lambda k: k['puntaje'],reverse=True)
    return render_to_response('resultados_orden.html', {'students': result}, context)