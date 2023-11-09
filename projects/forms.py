from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ['name', 'description', 'year', 'img', 'repository', 'technologies']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Projects Name'}),

            'description': forms.Textarea(attrs={'placeholder': 'Projects Description'}),

            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),

            'img': forms.ClearableFileInput(attrs={'placeholder': 'Select an Image'}),

            'repository': forms.URLInput(attrs={'placeholder': 'Repositiry URL'}), 
        }