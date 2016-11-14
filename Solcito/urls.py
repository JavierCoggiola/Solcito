from django.conf.urls import patterns, include, url
from Solcito import views, docentes_views, ordenes_de_merito

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
    url(r'^oredenes_de_merito/$', ordenes_de_merito.oredenes_de_merito, name="oredenes_de_merito"),
    url(r'^ordenar/$', ordenes_de_merito.ordenar, name="ordenar"),
]
