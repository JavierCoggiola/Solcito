from django.conf.urls import patterns, include, url
from Solcito import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_matricula/$', views.submitMatricula, name='submit_matricula'),
    url(r'^edit_matricula/$', views.editMatricula, name='edit_matricula'),
    url(r'^entrada$', views.entrada, name="entrada"),
    url(r'^buscador$', views.getFilter, name="buscador"),
    url(r'^search_student$', views.search, name="search_student"),
]
