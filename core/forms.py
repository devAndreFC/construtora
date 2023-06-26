from django import forms
from .models import Engineeer, Material, Project


class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineeer
        fields = '__all__'


class MateralForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
