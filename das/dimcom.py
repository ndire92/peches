from django.forms import ModelForm
from das.models import DimAgroCommercial
from django import forms


class AgroCommercial(ModelForm):

    ProdVenteSpecul = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeVente = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    MarchRegroupement = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ClientAgro = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimAgroCommercial
        fields = ['ProdVenteSpecul', 'TypeVente',
                  'MarchRegroupement', 'ClientAgro']
