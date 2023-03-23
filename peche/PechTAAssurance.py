from django.forms import ModelForm
from peche.models import DimPechTAAssurance
from django import forms


class petttassu(ModelForm):
    codeCommune= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
   
    OffreAssurTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypAssurTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPrimTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    BesoinformTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContraintGlobTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContrainMajFilierTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    
    class Meta:
        model = DimPechTAAssurance
        fields = ['codeCommune','nomCommune','OffreAssurTA', 'TypAssurTA', 'NivPrimTA',
                  'BesoinformTA', 'ContraintGlobTA', 'ContrainMajFilierTA','date','date_modification']
