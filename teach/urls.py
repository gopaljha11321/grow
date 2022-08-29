
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="teach_index"),
    path('check',views.check,name="check"),
    path('update',views.update,name="check"),
    path('reg',views.reg,name="reg"),
    # path('dashboard',views.dashboard,name="dashboard")
]
