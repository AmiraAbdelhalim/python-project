#urls redirection


from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views


	

urlpatterns =[
	
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', auth_views.LoginView.as_view(),name="login"),
	path('newPost/',views.newPost,name='newPost'),
	path('', views.PostList, name='home'),
	path('sub/<category_id>', views.subscribe, name ='subscribe'),
    path('unsub/<category_id>', views.unsubscribe, name ='unsubscribe'),
	path('home', views.home),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
	path('<slug>/<commentId>/',views.comment_reply,name="comment_reply"),
	
	
	# path('login/', views.SignUp.signup),
	
	# path('login/', auth_views.LoginView.as_view(),name="login"),
]