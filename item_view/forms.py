from django import forms
from . models import Item
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class upload_item(forms.ModelForm):


	class Meta:
		model = Item
		fields = ['item_name', 'item_description', 'item_price', 'item_image', 'item_category']


class update_item(forms.ModelForm):


	class Meta:
		model = Item
		fields = [ 'item_description', 'item_price']