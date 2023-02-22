from django.forms import ModelForm
from peche.models import DimPechTACommerc
from django import forms


class pectom(ModelForm):

    ProdVenduCampagTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypVentTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ModEcoulmtTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ClientTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPechTACommerc
        fields = ['ProdVenduCampagTA', 'TypVentTA', 'ModEcoulmtTA', 'ClientTA']
