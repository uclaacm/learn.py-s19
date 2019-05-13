"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views

# Whenever a request for a new page is made, Django goes through this list of url patterns until it
# finds one that matches the requested URL. If found, Django sends a request to the given view function 
# (the second parameter)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('darkMode/', views.dark_mode),
    path('piktures/<int:num>/', views.piktures),
]
