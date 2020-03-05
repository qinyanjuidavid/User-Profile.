from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import UserProfile



class ProfileUpdateForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=('bio','image')
class UserUpdateForm(ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username']
