from django.shortcuts import render
from usuarios.models import Paciente, Personal
from tutor.models import Consulta
from visita.models import Visita
from django.http import JsonResponse
from django.contrib.auth.models import Group
from datetime import datetime, date

def home(request):
	pacientes=Paciente.objects.all()
	personal=Personal.objects.count()
	current_user = request.user
	now = datetime.now()
	visita = Visita.objects.all()
	total = 100 #diferencia entre pacientes totales y pacientes para hoy
	hoy = 0
	completadas = 0

	for v in visita:
		if str(v.fecha) == str(date.today()):
			hoy = hoy + 1
			if v.status == 1:
				completadas = completadas + 1


	aux = 0
	for n in pacientes:
		if n.activo == 1:
			aux = aux + 1



	cont = 0
	consulta = Consulta.objects.all()
	for i in consulta:
		
		if i.estado == 0:
			cont = cont + 1


	completadas = (completadas*100)/hoy

	group = Group.objects.all() 
	context = {
			'pacientes':aux,
			'personal':personal,
			"actual":current_user,
			"group":group,
			"now":now,
			"total":total,
			"hoy":hoy,
			"realizadas":completadas,
			
	}
	return render(request,"dashboard.html", context)


def get_data_consulta(request,*args,**kwargs):

	con=Consulta.objects.filter(estado='0')
	consulta=con.count()
	data={
		"consulta":consulta,
	}
	return JsonResponse(data)
	