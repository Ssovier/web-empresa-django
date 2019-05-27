from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'contenido'}),
            'order': forms.NumberInput(attrs={'class': 'form-control','placeholder':'orden'}),
        }

        labels = {
            
        }
