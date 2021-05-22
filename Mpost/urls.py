from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.singUp,name="singup"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addpost/',views.addPost,name="add"),
    path('allpost/', views.allPost, name="allpost"),
    path('userLogout', views.userLogout, name='logout'),
]
