from django import forms
from orders.models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                 'address', 'postal_code', 'city']
        labels = {'first_name':'', 'last_name': '', 'email':'',
                  'address': '', 'postal_code':'', 'city':''}
        
        
        widgets = {
            'first_name': forms.fields.TextInput(attrs={
                'placeholder': 'Nome',
                'class': 'form-control',
            }),

            'last_name': forms.fields.TextInput(attrs={
                'placeholder': 'Sobrenome',
                'class': 'form-control',
            }),

            'email': forms.fields.TextInput(attrs={
                'placeholder': 'E-mail',
                'class': 'form-control',
            }),

            'address': forms.fields.TextInput(attrs={
                'placeholder': 'Endereço completo',
                'class': 'form-control',
            }),

            'postal_code': forms.fields.TextInput(attrs={
                'placeholder': 'CEP',
                'class': 'form-control',
            }),
            'city': forms.fields.TextInput(attrs={
                'placeholder': 'Cidade',
                'class': 'form-control',
            }),
        }