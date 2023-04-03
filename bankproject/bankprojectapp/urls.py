"""bankproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

app_name = 'bankprojectapp'

urlpatterns = [
    path('', views.index, name='index'),

    path('template/login', views.login, name="login"),
    path('template/register', views.register, name="register"),
    path('template/formpage', views.formpage, name="formpage"),
    path('template/logout/', views.logout, name="logout"),

]
