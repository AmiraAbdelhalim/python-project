#urls redirection
from django.urls import path
from blog import views


urlpatterns =[
	# path('register',views.register),
	# path('home', views.home),
	path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
	

]