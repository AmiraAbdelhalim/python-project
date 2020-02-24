from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.


def index(request):
	return render(request,'admin.html')


def posts(request):
	myPosts=Post.objects.all()
	context={'all_posts' : myPosts}
	return render(request,'posts.html',context)


def users(request):
	return render(request,'users.html')