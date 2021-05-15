from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label = "" , widget=forms.TextInput(attrs = {'type' : 'hidden'}))

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password' )
