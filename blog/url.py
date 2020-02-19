#urls redirection


from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from blog import views
from django.urls import path
from django.contrib.auth import views as auth_view



urlpatterns =[
	path('signup/', views.SignUp.as_view(), name='signup'),
	# path('login/', views.SignUp.signup),
	# path('home', views.home),
	path('login/', auth_views.LoginView.as_view(),name="login"),
]