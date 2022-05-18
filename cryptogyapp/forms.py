from django import forms

from cryptogyapp.models import *

class RsaForm(forms.ModelForm):
    class Meta:
        model = RSAInput
        fields = ("__all__")

class RsaDSSForm(forms.ModelForm):
    class Meta:
        model = RSADSSInput
        fields = ("__all__")

class RabinForm(forms.ModelForm):
    class Meta:
        model = RabinInput
        fields = ("__all__")

class MVForm(forms.ModelForm):
    class Meta:
        model = MVInput
        fields = ("__all__")

class GammalForm(forms.ModelForm):
    class Meta:
        model = GammalInput
        fields = ("__all__")

class GammalDSSForm(forms.ModelForm):
    class Meta:
        model = GammalDSSInput
        fields = ("__all__")