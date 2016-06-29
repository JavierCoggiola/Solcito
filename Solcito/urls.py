from django.conf.urls import patterns, include, url
from Solcito import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_matricula/$', views.submitMatricula, name='submit_matricula'),
    url(r'^edit_matricula/$', views.editMatricula, name='edit_matricula'),
    url(r'^entrada/$', views.entradaImg, name="entradaImg"),
    url(r'^solcito$', views.getFilter, name="solcito"),
    url(r'^search_student$', views.search, name="search_student"),
    url(r'^login/$', views.logMeIn, name='login'),
    url(r'^logout/$', views.logMeOut, name='logout'),
]
