from .models import Image
from django.forms import ModelForm, Form
from django import forms


class ImageForm(ModelForm, Form):
    image_url = forms.URLField(required=False, label='Ссылка')

    class Meta:
        model = Image
        fields = ['image']


class ResizeForm(Form):
    width = forms.IntegerField(required=False, label='Ширина', min_value=0)
    height = forms.IntegerField(required=False, label='Высота', min_value=0)
