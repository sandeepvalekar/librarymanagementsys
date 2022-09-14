"""LibraryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import Library
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from Library import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls') ),
     path('', views.home_view),

     path('adminclick', views.adminclick_view),

     path('adminsignup', views.adminsignup_view),
     path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
     path('logout', LogoutView.as_view(template_name='library/index.html')),
     path('afterlogin', views.afterlogin_view),

      path('book/create', views.BookCreateView.as_view(),
         name='book-create'),
      path('book/<int:pk>/update', views.BookUpdateView.as_view(),
         name='book-update'),
      path('book/<int:pk>/delete', views.BookDeleteView.as_view(),
         name='book-delete'),
      path('aboutus', views.aboutus_view),

]

