#urls redirection


from django.urls import path
from blog import views

urlpatterns =[
	path('signup',  views.SignUp.as_view(), name='signup'),
	path('home', views.home),

]