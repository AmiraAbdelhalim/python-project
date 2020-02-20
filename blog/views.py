from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
# from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from blog.forms import UserForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from blog.forms import UserForm
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserForm
    # success_url = reverse_lazy('login') #reverse_lazy to redirect the user to the login page upon successful registration.
    template_name = 'html/signup.html'
    # return httpResponseRedirect(success_url)

    def signup(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()

                user.save()

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect("login")
        else:
            form = UserForm()
            return render(request, 'html/signup.html', {'form': form})




