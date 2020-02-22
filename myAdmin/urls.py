#urls redirection


from django.urls import path
from myAdmin import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name='myAdmin'
	

urlpatterns =[
	
	url(r'^$',views.index),
]
