#urls redirection


from django.urls import path
from myAdmin import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name='myAdmin'
	

urlpatterns =[
	
	url(r'^$',views.index),
	path('users', views.users),
	path('posts', views.posts),
	path('editUser/<id>',views.editUser),
	path('deleteUser/<id>',views.deleteUser),
	path('addUser', views.addUser),
	path('viewUser/<id>', views.viewUser),
	path('viewAdmin', views.viewAdmin),
	path('adminInfo/<id>', views.adminInfo),

]
