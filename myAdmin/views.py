from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	return render(request,'admin.html')


def posts(request):
	return render(request,'posts.html')


def users(request):
	return render(request,'users.html')