from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,UpdateView
from Task.models import Task
from Task.forms import RegistrationForm,LoginForm,TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from Task.models import Task
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication

class TodoSerializer(serializers.ModelSerializer):
    user= serializers.CharField(read_only=True)
    created_date= serializers.DateTimeField(read_only=True)
    class Meta:
        model=Task
        fields=['task_name','user','created_date']

class TodosView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Task.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
def signin_reqiured(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"You must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")

@method_decorator(signin_reqiured,name="dispatch")
class Add_todo_View(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_task.html")

    def post(self,request,*args,**kwargs):
        user = request.user
        task = request.POST.get("task")
        Task.objects.create(user=request.user,task_name=task)
        messages.success(request,"task created")
        return redirect("todo-all")

@method_decorator(signin_reqiured,name="dispatch")
class Task_List_View(ListView):
    model = Task
    template_name = "task-list.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:

    #         qs = Task.objects.filter(user=request.user)
    #         return render(request,"task-list.html",{"todos":qs})
    #     else:
    #         return redirect("signin")

@method_decorator(signin_reqiured,name="dispatch")
class Task_Detail_View(DetailView):
    model = Task
    template_name = "task-detail.html"
    context_object_name = "todo"
    pk_url_kwarg = "id"

    # def get(self,request,*args,**kwargs):
    #     id = kwargs.get("id")
    #     task = Task.objects.get(id=id)
    #     return render(request,"task-detail.html",{"todo":task})

@method_decorator(signin_reqiured,name="dispatch")
class Task_Delete_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Task.objects.get(id=id).delete()
        messages.success(request,"task deleted")
        return redirect("todo-all")

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"account created")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("todo-all")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})

@signin_reqiured
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("register")

class Task_Update_View(UpdateView):
    model = Task
    template_name = "todo-update.html"
    form_class = TaskUpdateForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("todo-all")

#django -> views -> generic -> class View()
#                              class ListView()
#                              class DetailView()
#                              class UpdateView()
#                              class DeleteView()
#                              class CreateView()
#                              class TemplateView()
#                              class FormView()

