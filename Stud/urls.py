"""Stud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include

from django.contrib.auth.views import LoginView, LogoutView

from .import views
from django.contrib import admin
from django.urls import path
from .import Hod_views, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin', admin.site.urls),
    path('base', views.Base, name='base'),
    path('home', Hod_views.Home, name='home'),
    # path('foncier_home', Staff_views.Home, name='foncier_home'),
    # profile
    path('', views.Accueil, name='acceueil'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('peche/', views.peche, name="peche"),
    path('post/<int:id>/', views.detail, name="detail"),
    path('post/', views.all, name="post"),
    path('new_post', views.new_post, name="new_post"),
    path('update_post/<int:pk>/', views.update_post, name="update_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('ressource/',views.ress,name="ressource"),
    path('upda_res/<int:id>/',views.upda_ress,name="upda_res"),
    path('delete_ress/<int:id>/',views.del_ress,name="delete_ress"),
    
    #path('add_prof', views.add_profile, name='add_prof'),
    #path('profil/update/<int:id>/', views.update_profile, name='update_profile'),
  
    #path('users/update/', views.Cupdate, name='users_update'),
    #path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    #path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    #path('create/', views.ProfileCreateView.as_view(), name='profile_create'),
    #path('<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
     #path('<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),

    # url home
#    path('home', include('home.urls')),


    path('peche/', include('peche.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
