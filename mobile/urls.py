"""mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mobileapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Project, name='project'),
    path('access.html', views.Access, name='access'),
    path('camera.html', views.Camera, name='camera'),
    path('color.html', views.Color, name='color'),
    path('home.html', views.Home, name='home'),
    path('phone.html', views.Phone, name='phone'),
    path('form.html', views.load_form, name="form"),
    path('add', views.add, name="add"),
    path('show', views.show, name="show"),
]