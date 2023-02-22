from django.forms import ModelForm
from peche.models import DimPecheInnovat
from django import forms


class pecino(ModelForm):

    TechnoIntrod= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TechnoAdopte = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CausNoAdoption= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CausTechnoNoAdop = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    


    class Meta:
        model = DimPecheInnovat
        fields = ['TechnoIntrod','TechnoAdopte','CausNoAdoption','CausTechnoNoAdop']