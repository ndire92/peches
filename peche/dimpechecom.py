from django.forms import ModelForm
from peche.models import DimPecheCommerce
from django import forms


class DPC(ModelForm):

    ProdVendType = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ProdVendCampgnHiver = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ProdVendCampgnInterSais = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ProdVendCampSaisFroid = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ProdVendCampPrintem = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Type_VentPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Mod_ecoulement = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ClientPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPecheCommerce
        fields = ['ProdVendType', 'ProdVendCampgnHiver', 'ProdVendCampgnInterSais',
                  'ProdVendCampSaisFroid', 'ProdVendCampPrintem', 'Type_VentPech', 'Mod_ecoulement', 'ClientPech']
