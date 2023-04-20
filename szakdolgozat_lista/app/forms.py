from django.forms import ModelForm, ValidationError
from app.models import *
from django import forms

class Szakdogaform(ModelForm):
    class Meta:
        model = Szakdoga
        fields = '__all__'