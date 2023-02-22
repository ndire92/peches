from django.forms import ModelForm
from peche.models import DimPechTAAssurance
from django import forms


class petttassu(ModelForm):

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

    class Meta:
        model = DimPechTAAssurance
        fields = ['OffreAssurTA', 'TypAssurTA', 'NivPrimTA',
                  'BesoinformTA', 'ContraintGlobTA', 'ContrainMajFilierTA']
