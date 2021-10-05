"""mysite URL Configuration

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
from blogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),   
    path('blog/', views.blog, name='blog'),   
    path('contact/', views.contact, name='contact'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.SignUp, name='signup'),   
    path('login/', views.log, name='login'),   
    path('logout/', views.logoutdata, name='logout'),   
    path('adddata/', views.add_item, name='adddata'),   
    path('update/<int:id>/', views.update_data, name='updatedata'),    
    path('delete/<int:id>/', views.delete_data, name='deletedata'),    




]
