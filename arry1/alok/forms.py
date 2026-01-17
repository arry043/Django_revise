from django import forms
from .models import AlokVarity

class AlokVarityForm(forms.ModelForm):
    class Meta:
        model = AlokVarity
        fields = ['name', 'type', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Enter Alok name'
            }),
            'type': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500',
            }),
        }
