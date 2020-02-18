from django.shortcuts import render
from django.urls import reverse_lazy #where if user logged in or logged out where should be directed
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('login')
    template_name = 'html/signup.html'

def home(request):
    return render(request, 'html/index.html')


# def register(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect("/blog/home")
#     else:
#         user_form= UserForm()
#         context= {'user_form': user_form}
#         return render(request, 'html/register.html', context)


