from django.shortcuts import render,redirect
from django.views.generic import View
from Task.models import Task
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

    def post(self,request,*args,**kwargs):
        name = request.POST.get("username")
        task = request.POST.get("task")
        Task.objects.create(user=name,task_name=task)
        return render(request,"add_todo.html")

class Task_List_View(View):
    def get(self,request,*args,**kwargs):
        qs = Task.objects.all()
        return render(request,"task-list.html",{"todos":qs})

class Task_Detail_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        task = Task.objects.get(id=id)
        return render(request,"task-detail.html",{"todo":task})

class Task_Delete_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Task.objects.get(id=id).delete()
        return redirect("todo-all")