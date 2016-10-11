from django.conf.urls import patterns, include, url
from Solcito import views, docentes_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registration/$', views.index, name='index'),
    url(r'^submit_matricula/$', views.submitMatricula, name='submit_matricula'),
    url(r'^login/$', views.logMeIn, name='login'),
    url(r'^logout/$', views.logMeOut, name='logout'),
    url(r'^genpdf/(?P<id_student>[0-9]+)/$', views.genpdf, name="genpdf"),
    url(r'^confirm_matricula/$', views.confirmMatricula, name='confirm_matricula'),
    url(r'^docentes/$', docentes_views.docentes, name="docentes"),
    url(r'^excel/$', docentes_views.excel, name="excel"),
]
