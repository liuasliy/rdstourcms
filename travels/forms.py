#coding=utf-8
from django.forms import ModelForm
from travels.models import *
from django import forms



class UserForm(ModelForm):


    class Meta:
      model = Travels