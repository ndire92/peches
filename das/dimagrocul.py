from django.forms import ModelForm
from das.models import DimAgroCulture
from django import forms


class DimAgrocultf(ModelForm):

    ZonProd_Cult = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Cultur_Pratique = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Type_Semence = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Type_Culture_Pratique = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    VarieteCultive = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisIntran = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisSemenc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisEngrProdPhyto = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisMatAgro = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeAcquisIntran = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeAcquisMat = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '   ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeFertilisUtil = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypePesticidUtil = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ModAcquisParcel = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '   ', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimAgroCulture
        fields = ['ZonProd_Cult', 'Cultur_Pratique', 'Type_Semence', 'Type_Culture_Pratique', 'VarieteCultive', 'SourcApprovisIntran', 'SourcApprovisSemenc',
                  'SourcApprovisEngrProdPhyto', 'SourcApprovisMatAgro', 'TypeAcquisIntran', 'TypeAcquisMat', 'TypeFertilisUtil', 'TypePesticidUtil', 'ModAcquisParcel']
