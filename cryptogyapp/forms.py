from django import forms
from cryptogyapp.models import RSAInput

class RsaForm(forms.Form):
    primeP = forms.IntegerField(label='Prime number (p)', required=True)
    primeQ = forms.IntegerField(label='Prime number (q)', required=True)
    clearText = forms.CharField(label='Cleartext', widget=forms.Textarea, required=False)    
    cipherText = forms.CharField(label='Ciphertext', widget=forms.Textarea, required=False)

class RabinForm(forms.ModelForm):
    primeP = forms.IntegerField(label='Prime number (p)', required=True)
    primeQ = forms.IntegerField(label='Prime number (q)', required=True)
    clearText = forms.CharField(label='Cleartext', widget=forms.Textarea, required=False)    
    cipherText = forms.CharField(label='Ciphertext', widget=forms.Textarea, required=False)