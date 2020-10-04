"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class DataForm(forms.Form):
    Revenue = forms.CharField(label='Revenue', max_length=100)
    Cost = forms.CharField(label='Cost', max_length=100)
    Lease = forms.CharField(label='Lease', max_length=100)
    Utilities = forms.CharField(label='Utilities', max_length=100)
    Product = forms.CharField(label='Product', max_length=100)
    Assets = forms.CharField(label='Assets', max_length=100)

    fields = ('Revenue', 'Cost', 'Lease', 'Utilities', 'Product', 'Assets')
    widgets = {
        'Revenue': forms.TextInput(attrs={'class': 'form-control'}),
        'Cost': forms.TextInput(attrs={'class': 'form-control'}),
        'Lease': forms.TextInput(attrs={'class': 'form-control'}),
        'Utilities': forms.TextInput(attrs={'class': 'form-control'}),
        'Product': forms.TextInput(attrs={'class': 'form-control'}),
        'Assets': forms.TextInput(attrs={'class': 'form-control'}),
    }

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
