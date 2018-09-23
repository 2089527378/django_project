"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")# project_name 项目名称
django.setup()
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('', views.get1,name='index'),
    path('tree/', views.get, name='tree'),
    path('admin/', admin.site.urls),
    url(r'doc/', include_docs_urls(title='b')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
