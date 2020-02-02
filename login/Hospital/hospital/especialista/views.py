from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from usuarios.models import Personal , Paciente, Perfil
'''from .forms import PostForm'''
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from biblioteca.models import Archivo
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return render(request,"main.html")


def home_especialista(request):
	current_user = request.user
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)

	context = {

		"actual": current_user,	
		"personal":px,

	}
	return render(request,"index_especialista.html",context)


def ver_perfil_e (request):

	current_user = request.user
	group=Group.objects.all()
	for g in group:
		if g.id != '1' and g.id != '2' and g.id != '20':
			user=User.objects.filter(groups__id=g.id)
			name=g.name

	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	tl = get_object_or_404(Perfil,id=current_user.id)
	

	context = {

		"actual": current_user,
		"personal":px,
		"tel":tl.tel,
		"users_group":user,
		"name_group":name

	}
	return render(request,"ver_perfil_e.html",context)

def biblioteca_e(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_especialista.html',{'archivo':archivo})


def Especialista_edit(request,perfil=None,id_personal=None):
	
	personal=Personal.objects.get(id=id_personal)
	if request.method=='GET':
		form=Personal_Form(instance=personal)
	else:
		form=Personal_Form(request.POST,instance=personal)
		if form.is_valid():
			form.save()
		return redirect(ver_perfil_e)
	return render(request,'personal_f.html',{'form':form,'perfil':perfil})
