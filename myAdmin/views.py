from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User as Users
from blog.models import Post, Category
from myAdmin.forms import UserForm, CategoryForm
from blog.forms import PostForm
# Create your views here.


def index(request):
	return render(request,'admin.html')


def posts(request):
	myPosts=Post.objects.all()
	context={'all_posts' : myPosts}
	return render(request,'posts.html',context)


def users(request):
	all_users= Users.objects.all()
	context={'all_users': all_users}
	return render(request,'users.html', context)

def addUser(request):
	if request.method=="POST":
		user_form=UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect("/admin/users")
		else:
			print("fail")
	else:
		user_form=UserForm()
		context={'user_form': user_form}
		return render(request,"user_add.html", context)

def editUser(request, id):
	user=Users.objects.get(id=id)
	if request.method=="POST":
		# print("hello post")
		user_form=UserForm(request.POST, instance=user)
		if user_form.is_valid():
			# print("hello valid")
			user_form.save()
			return HttpResponseRedirect("/admin/users")
	else:
		user_form=UserForm(instance=user)
		context={'user_form':user_form}
		return render (request,'user_add.html', context)

def deleteUser(request, id):
	user=Users.objects.get(id=id)
	user.delete()
	return HttpResponseRedirect("/admin/users")


def viewUser(request, id):
	user=Users.objects.get(id=id)
	context={'user':user}
	return render (request, 'user_details.html', context)


def viewAdmin(request):
	admin=Users.objects.filter(is_staff=True)
	# if admin.is_staff==True:

		# print(admin)
	context={'admin':admin}
	return render(request, 'viewAdmin.html', context)

def adminInfo(request, id):
	
	admin=Users.objects.get(id=id)
	context={'admin':admin}
	return render (request, 'admin_info.html', context)

def viewCategories(request):
	cat=Category.objects.all()
	context={'all_cat': cat}
	return render (request, 'categories.html',context)

def addCat(request):
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/admin/viewCategories")
	else:
		form=CategoryForm()
		context={'form': form}
		return render(request,"catAdd.html",context)


def viewCat(request, id):
	cat=Category.objects.get(id=id)
	myPosts=Post.objects.all()

	context={'cat':cat,
			 'myPosts':myPosts
	}
	return render (request, 'cat_details.html', context)

def deleteCat(request, id):
	cat=Category.objects.get(id=id)
	cat.delete()
	return HttpResponseRedirect("/admin/viewCategories")

def editCat(request,id):
	cat = Category.objects.get(id=id)
	if request.method == 'POST':
		form = CategoryForm(request.POST,instance=cat)
		if form.is_valid():
			form.save()
			return  HttpResponseRedirect("/admin/viewCategories")
	else:
		form = CategoryForm(instance=cat)
		context = {'form':form}
		return render(request,"catAdd.html",context)