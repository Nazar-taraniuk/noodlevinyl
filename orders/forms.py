from django import forms
from .models import VinylOrder

class VinylOrderForm(forms.ModelForm):
    class Meta:
        model = VinylOrder
        exclude = ['user', 'price', 'created_at']

