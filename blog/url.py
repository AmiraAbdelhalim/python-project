# urls redirection


from django.urls import path 
from django.conf.urls import url
from blog import views
from django.contrib.auth import views as auth_views



	

urlpatterns =[
	
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', auth_views.LoginView.as_view(),name="login"),
	path('logout/',auth_views.LogoutView.as_view(), name="logout"),
	path('newPost/',views.newPost,name='newPost'),
	path('', views.PostList, name='home'),
	path('sub/<category_id>', views.subscribe, name ='subscribe'),
    path('unsub/<category_id>', views.unsubscribe, name ='unsubscribe'),
	path('home', views.home),
	path('search/',views.search,name='search'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
	path('<slug>/<commentId>/',views.comment_reply,name="comment_reply"),
	path('<slug>/<postID>/l/',views.liked,name='liked'),
	path('<slug>/<postID>/d/',views.disliked,name='disliked'),
	# url(r'^blog/first-blog/(?P<postID>[\w])/$', views.liked),
    # url(r'^(?P<postID>[\w])/(?P<postTitle>[\w]+)/d/$', views.disliked),
	path('editPost/<slug:slug>',views.editPost),

	
	# path('login/', views.SignUp.signup),
	
	# path('login/', auth_views.LoginView.as_view(),name="login"),
]

