"""newproject URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from newapp import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.show,name='show'),
    path('blog/',views.djangof,name='blog'),
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('delete<int:id>',views.delete ,name='delete'),
    path('update<int:id>',views.update ,name='update'),
    path('about/',views.about,name='about')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
