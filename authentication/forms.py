from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import  DaemonStar_User

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = DaemonStar_User
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = DaemonStar_User
		fields = ('username', 'email')



class LoginForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)

	class Meta:
		model = DaemonStar_User
		fields = ['username', 'password']

