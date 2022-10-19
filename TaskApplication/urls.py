"""TaskApplication URL Configuration

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
from django.contrib import admin
from django.urls import path
from Task.views import IndexView,LoginView,RegisterView,Add_todo_View, RegistrationView,Task_List_View,Task_Detail_View,Task_Delete_View,RegistrationView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",IndexView.as_view()),
    path("login/",LoginView.as_view()),
    path("register/",RegisterView.as_view()),
    path("todo/add/",Add_todo_View.as_view(),name="todo-add"),
    path("todos/all",Task_List_View.as_view(),name="todo-all"),
    path("todos/<int:id>/detail",Task_Detail_View.as_view(),name="todo-detail"),
    path("todos/<int:id>/delete",Task_Delete_View.as_view(),name="todo-delete"),
    path("accounts/register",RegistrationView.as_view(),name="register"),
    path("accounts/login",LoginView.as_view(),name="signin")
    
]
