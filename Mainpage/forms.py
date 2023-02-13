from django import forms
from .models import Profiles

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ["profile_img"]
        labels = {"profile_img": ""}