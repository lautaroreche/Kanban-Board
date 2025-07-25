"""
URL configuration for kanban project.

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
from django.urls import path
from kanban_app.views import home, change_status, create, view, edit, delete, toggle_focus
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('change_status/<int:task_id>/<str:direction>/', change_status, name='change_status'),
    path('create/', create, name='create'),
    path('view/', view, name='view'),
    path('view/<int:task_id>/', view, name='view'),
    path('edit/<int:task_id>/', edit, name='edit'),
    path('delete/<int:task_id>/', delete, name='delete'),
    path('toggle_focus/<int:task_id>/', toggle_focus, name='toggle_focus'),
]
