from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^hello-world/$', views.hello_world, name='hello_world'),

]
