from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
path('',views.index,name="index"),
path('login',views.index_verify,name="Login"),
path('verify',views.login,name="check"),
path('update',views.update,name="update")
]
