from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from Solcito.forms import UploadForm
from Solcito.models import Student, Teacher, Marks, RegistrationD, trim, RegistrationS, Subject
import openpyxl
import xlrd

@login_required(login_url='/login/')
def docentes(request):
    context = RequestContext(request)
    if request.user.groups.filter(name='Docente').exists():
        matriculas = RegistrationD.objects.filter(teacher=request.user.teacher)
        trimestres =  trim
        return render_to_response('docentes.html', {'matriculas': matriculas, 'trimestres' : trimestres}, context)
    else:
        return redirect('/admin')



def excel(request):
    context = RequestContext(request)
    input_excel = request.FILES['docfile']
    materia = request.POST['materia']
    trimestre = request.POST['trimestre']
    book = xlrd.open_workbook(file_contents=input_excel.read())
    rows = []
    # leer hoja 1
    sh = book.sheet_by_index(0)
    print trimestre
    if trimestre == '1':
        offset = 7
    elif trimestre == '2':
        offset = 11
    elif trimestre == '3':
        offset = 16
    else:
        offset = 7
    # fortuna row 15 col 2
    breaking = False
    print materia
    for i, row in enumerate(range(sh.nrows)):
        if i <= offset:  # (Optionally) skip headers
            continue
        r = []
        for j, col in enumerate(range(sh.ncols)):
            if (sh.cell_value(i, 2)) != "":
                r.append(sh.cell_value(i, j))
            else:
                breaking = True
                break
        if breaking:
            break
        rows.append(r)

    # Guardar los datos del excel en la base de datos
    for i in rows:
        newMark = Marks()
        try:
            newMark.reg = RegistrationS.objects.filter(student__lastName__icontains=i[2].split(", ")[0],
                                                       student__name__icontains=i[2].split(", ")[1],)[0]
            newMark.subject = Subject.objects.get(pk=materia)
            newMark.trim = trimestre
            newMark.nota = i[offset]
            newMark.save()
        except IndexError:
            pass

    return render_to_response('docentes.html', {'rows': rows}, context)


def createModels(request):
    context = RequestContext(request)
    for i in rows:
        newalumn = Student(name=i[2], nota=i[7])
        newalumn.save()
    return render_to_response('index.html', {}, context)