#urls redirection
from django.urls import path
from blog import views

urlpatterns =[
	path('register',views.register),
	path('home', views.home),

]