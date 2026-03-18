"""
URL configuration for expert_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from diagnoses import urls as diagnoses_urls
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('admin/', admin.site.urls),
    path('diagnose/login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('diagnose/logout/', RedirectView.as_view(url='/accounts/logout/', permanent=False)),
    path('diagnose/', include(diagnoses_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/diagnose/', permanent=False)),
]
