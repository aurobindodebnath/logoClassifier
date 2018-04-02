from .models import ImageModel
from django import forms

class ImageModelForm(forms.ModelForm):
	class Meta:
		model= ImageModel
		fields = ["img"]