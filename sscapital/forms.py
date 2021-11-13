from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Ledger, Prometheus

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control rounded-4',
        'id' : 'floatingInput',
        'placeholder' : 'name@example.com'
    }))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password',
        'class':'form-control rounded-4',
        'type': 'password',
        'id': 'floatingPassword',
        'placeholder': 'Password'
    }))

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ['investor', 'transaction', 'money_moved']

        widgets = {'investor': forms.Select(attrs={'class': 'form-select', 'id': 'investor'}),
            'transaction': forms.Select(attrs={'class': 'form-select', 'id': 'transaction'}),
            'money_moved': forms.NumberInput(attrs={'class': 'form-control', 'id': 'money_moved', 'placeholder': 'Funds'}),
        }

class UpdatePrometheus(forms.ModelForm):
    class Meta:
        model = Prometheus
        fields = ['value']

        widgets = {
            'value': forms.NumberInput(attrs={'class': 'form-control', 'id': 'value', 'placeholder': 'Funds'}),
        }