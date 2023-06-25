from django import forms
from .models import Engineeer, Material


class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineeer
        fields = '__all__'


class MateralForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
