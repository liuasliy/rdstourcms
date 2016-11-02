#coding=utf-8
from django.forms import ModelForm
from travels.models import *
from django import forms
from userena.forms import *
from userena.models import *
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.models import *



class userpassForm(ModelForm):


    class Meta:
      #model = UserenaSignup
      model = User
      fields = '__all__'