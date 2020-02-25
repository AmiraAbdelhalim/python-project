# urls redirection


from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('home', views.home),
    
]
