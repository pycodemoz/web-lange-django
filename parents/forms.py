from django import forms
from .models import Parent


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'last_name', 'photo', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }
        
        labels = {
            'name': 'Nome',
            'last_name': 'Sobrenome',
            'photo': 'Foto',
            'birthday': 'Data de Nascimento'
        }
        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Garante que o formato de entrada também seja aceito
            self.fields['birthday'].input_formats = ['%Y-%m-%d']
        
       
        
