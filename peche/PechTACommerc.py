from django.forms import ModelForm
from peche.models import DimPechTACommerc
from django import forms


class pectom(ModelForm):
    codeCommune= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
   
    ProdVenduCampagTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypVentTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrixVentMoyProdTA = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ModEcoulmtTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ClientTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    datet= forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    
    class Meta:
        model = DimPechTACommerc
        fields = ['codeCommune','nomCommune','ProdVenduCampagTA', 'TypVentTA','PrixVentMoyProdTA', 'ModEcoulmtTA', 'ClientTA','datet','date_modification']
