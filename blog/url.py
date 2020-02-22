#urls redirection


from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views


	

urlpatterns =[
	
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', auth_views.LoginView.as_view(),name="login"),
	path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
	path('signup/login/home', views.home),
	# path('login/', views.SignUp.signup),
	
	# path('login/', auth_views.LoginView.as_view(),name="login"),
]