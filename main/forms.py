from django import forms
from .models import Vinyl

class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-white'}),
            'price': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark text-white'}),
            'long_description': forms.Textarea(attrs={'class': 'form-control bg-dark text-white'}),
        }
