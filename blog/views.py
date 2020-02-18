from django.shortcuts import render
from blog.models import User
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import UserForm


# Create your views here.
# Create your views here.

def home(request):
    return render(request, 'html/index.html')


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/blog/home")
    else:
        user_form= UserForm()
        context= {'user_form': user_form}
        return render(request, 'html/register.html', context)


