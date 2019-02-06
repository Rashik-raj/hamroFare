from typing import Dict, Any
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Superadmin
from company.models import Company, Device
from user.models import User, Transaction, Card

def login(request):
	if request.method == 'POST':
		name = request.POST['userName']
		password = request.POST['password']
		login = Superadmin.objects.filter(username=name, password=password)
		if not login:
			err_msg = "Login Invalid"
			context = {'err_msg': err_msg}
			return render(request, 'superadmin/index.html', context)
		else:
			user = User.objects.all()
			company = Company.objects.all()

			request.session['Superuser'] = name
			return render(request, 'superadmin/index.html', {'user': user, 'company' : company})

	return render(request, 'superadmin/login.html')

def index(request):
	if 'Superuser' in request.session:
		user = User.objects.all()
		company = Company.objects.all()
		return render(request, 'superadmin/index.html', {'user': user, 'company' : company})
	else:
		return redirect('superadmin:login')




def logout(request):
	if 'Superuser' in request.session:
		del request.session['Superuser']
	return redirect('superadmin:login')
