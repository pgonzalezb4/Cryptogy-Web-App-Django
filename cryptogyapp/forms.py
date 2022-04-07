from django.forms import ModelForm
from django import forms

from cryptogyapp.models import RSAInput, RabinInput

class RsaForm(forms.ModelForm):
    class Meta:
        model = RSAInput
        fields = ("__all__")

class RabinForm(forms.ModelForm):
    class Meta:
        model = RabinInput
        fields = ("__all__")