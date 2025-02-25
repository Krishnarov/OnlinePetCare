"""
URL configuration for petcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='index',),
    path("gallery/",views.gallery,name='gallery',),
    path("services/",views.services,name='services',),
    path("blog/",views.blog,name='blog',),
    path("login/",views.login,name='login',),
    path("signup/",views.signup,name='signup',),
    path("adminhome/",views.adminhome,name='adminhome',),
    path('upload/', views.upload_image, name='upload_image'),
    path('cards/', views.cards, name='cards'),
    path('viewenquiry/', views.viewenquiry, name='viewenquiry'),
    path('delete-slider/<int:id>/', views.delete_slider, name='delete_slider'),
    path('delete-cards/<int:id>/', views.delete_cards, name='delete_cards'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)