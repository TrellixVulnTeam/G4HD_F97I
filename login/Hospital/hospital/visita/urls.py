from django.conf.urls import url,re_path
from django.urls import path, include
from visita import views

urlpatterns =[

url(r'hora/(?P<id>\d+)$',views.agendar_visita, name="agendar_visita"),
url(r'lista/',views.agendar_lista, name="agendar_lista"),
url(r'paciente/',views.visita_paciente, name="visita_paciente"),

]