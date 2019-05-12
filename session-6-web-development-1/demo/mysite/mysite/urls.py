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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

# Whenever a request for a new page is made, Django finds the urlpatterns variable, and goes through the list until
# finds the one that matches the requested URL. If found, Django calls the given view, whose definitions are in views.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('darkMode/', views.dark_mode),
    path('piktures/', views.piktures_home),
    path('piktures/<int:num>', views.piktures)
]

urlpatterns += staticfiles_urlpatterns()
