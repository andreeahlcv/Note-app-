from django.urls import path
from . import views 

urlpatterns=[
    path('', views.home, name='Home'),
    path('home', views.home, name='Home'),
    path('sing-up', views.sing_up, name='sing_up'),
    path('create-post', views.create_post, name='create_post'),
]