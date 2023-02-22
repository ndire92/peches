from django.forms import ModelForm
from foncier.models import DimFoncier
from django import forms


class Dimfonfon(ModelForm):
    TypeFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    StatuFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TerrDeclas5D_Ans = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ActFonciePresen = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TxtFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    OutilGesFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    TypeConflit = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeUsage = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ExistCadrConcert = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EchelCadrConcert = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Entrepris_Indust_IncidFonc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeExploit_Foncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimFoncier
        fields = ['TypeFoncier', 'StatuFoncier', 'TerrDeclas5D_Ans', 'ActFonciePresen', 'TxtFoncier', 'OutilGesFoncier',
                  'TypeConflit', 'TypeUsage', 'ExistCadrConcert', 'EchelCadrConcert', 'Entrepris_Indust_IncidFonc', 'TypeExploit_Foncier']
