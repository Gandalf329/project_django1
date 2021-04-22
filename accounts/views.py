from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.db import models
from sports.models import Articles


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")
    
    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email" )

class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    news = Articles.objects.all()
    
    return render(request,'accounts/profile.html',{'news':news})