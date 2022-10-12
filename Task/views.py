from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")

class Add_todo_View(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_todo.html")