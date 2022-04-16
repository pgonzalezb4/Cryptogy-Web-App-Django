from django import forms

from cryptogyapp.models import *

class RsaForm(forms.ModelForm):
    class Meta:
        model = RSAInput
        fields = ("__all__")

class RabinForm(forms.ModelForm):
    class Meta:
        model = RabinInput
        fields = ("__all__")

class MVForm(forms.ModelForm):
    class Meta:
        model = MVInput
        fields = ("__all__")