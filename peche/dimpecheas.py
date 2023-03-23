from django.forms import ModelForm
from peche.models import DimPecheAssure
from django import forms


class DPAS(ModelForm):
    codeCommune  = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    OffreAssureExistPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeAssurancPech =forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSouscripPech  = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePrimePech  = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    BesoinFormatPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ActeurSensibilisePech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ActeurFormatPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    BesoinSensibilisePech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContraintGlobPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContrainMajFilier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrInfrastruStokCondition = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrFourniEmblag = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrProdLabel = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    
    class Meta:
        model = DimPecheAssure
        fields = ['codeCommune',
                    'nomCommune',
                    'OffreAssureExistPech',
                    'TypeAssurancPech',
                    'NbreSouscripPech',
                    'NbrePrimePech',
                    'BesoinFormatPech',
                    'ActeurSensibilisePech',
                    'ActeurFormatPech',
                    'BesoinSensibilisePech',
                    'ContraintGlobPech',
                    'ContrainMajFilier',
                    'NbrInfrastruStokCondition',
                    'NbrFourniEmblag',
                    'NbrProdLabel',
                    'date','date_modification']
