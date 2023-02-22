from django.forms import ModelForm
from foncier.models import DimFoncierGouvernanc
from django import forms


class Dimfong(ModelForm):

    LoiReglement = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    OutilSecuriseFoncie = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    ActFoncier = forms.CharField(label='act fonfier', widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DegreConnaissanc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))

    NivComprehension = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    Resume = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    AtelierBonInformat = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    SecuritAjout = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    ActImplique = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    CauseAvance = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    SolutionPropose = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    SolutionRetenu = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    VerificatProcedur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 900px;', 'class': 'form-control'}))
    ControlPermanant = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = DimFoncierGouvernanc
        fields = ['LoiReglement', 'OutilSecuriseFoncie', 'ActFoncier', 'DegreConnaissanc',
                  'NivComprehension', 'Resume', 'AtelierBonInformat', 'SecuritAjout', 'ActImplique',
                  'CauseAvance', 'SolutionPropose', 'SolutionRetenu', 'VerificatProcedur', 'ControlPermanant']
