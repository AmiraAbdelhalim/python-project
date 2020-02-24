from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User as Users
# Create your views here.


def index(request):
	return render(request,'admin.html')


def posts(request):
	return render(request,'posts.html')


def users(request):
	all_users= Users.objects.all()
	context={'all_users': all_users}
	return render(request,'users.html', context)