from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class RegisterForm(UserCreationForm):
   email = forms.EmailField(label='Email')
  
   class Meta:
     model = User
     fields = ["email", "username", "password", "password2"]

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class EditProfileForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ['email', 'username']
    
class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_image', 'bio']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

class PostPicForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image', 'image-caption']