from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta():
        model = Image
        # fields = ('image','caption_1')
        fields = ('image','caption_1','caption_2','caption_3','caption_4','caption_5')
        labels = {'image':''}

