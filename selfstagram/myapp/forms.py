from django import forms 
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo']
        labels = {'photo': 'Choose a photo'}

