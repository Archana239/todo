from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-primary","placeholder":"enter first name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-primary","placeholder":"enter last name"}),
            "username":forms.TextInput(attrs={"class":"form-control border border-primary","placeholder":"enter username"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-primary","placeholder":"enter your email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control border border-primary","placeholder":"enter password"})
        }
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-primary","placeholder":"enter username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control border border-primary","placeholder":"enter password"}))
    
        