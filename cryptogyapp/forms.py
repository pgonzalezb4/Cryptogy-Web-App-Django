from django.forms import ModelForm
from django import forms

from cryptogyapp.models import RSAInput

class RsaForm(forms.ModelForm):
    class Meta:
        model = RSAInput
        fields = ("__all__")

class RabinForm(forms.Form):
    primeP = forms.IntegerField(label='Prime number (p)', required=False)
    primeQ = forms.IntegerField(label='Prime number (q)', required=False)
    clearText = forms.CharField(label='Cleartext', widget=forms.Textarea, required=False)    
    cipherText = forms.CharField(label='Ciphertext', widget=forms.Textarea, required=False)