from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from Solcito.models import Imagen
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
    return render_to_response('matricular.html',{},context)
