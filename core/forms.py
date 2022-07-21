
from django import forms
from core.models import Example
class ExampleForm(forms.ModelForm):
    class Meta:
        model=Example
        fields='__all__'
    
        widgets = {
            'name': forms.TextInput(attrs={'palceholder':'Название'}),
            'color': forms.TextInput(attrs={'placeholder':'цвет'}),
            'cost': forms.NumberInput(attrs={'placeholder':'Цена'})
        }