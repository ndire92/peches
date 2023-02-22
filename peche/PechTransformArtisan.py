from django.forms import ModelForm
from peche.models import DimPechTransformArtisan
from django import forms


class pectranf(ModelForm):
    ActTransfArtisan = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    GrptTransformtrTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypServicOffrGIE = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypServicOffrAssocia = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    TypServicOffrOrgProf = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MatEquipTransExist = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdTransfPeriod = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApproIntranMatTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    QteProdPeriodTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    QteProdTypeTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauxTransformArtisan = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPechTransformArtisan
        fields = ['ActTransfArtisan', 'GrptTransformtrTA', 'TypServicOffrGIE', 'TypServicOffrAssocia',
                  'TypServicOffrOrgProf', 'MatEquipTransExist', 'TypProdTransfPeriod', 'SourcApproIntranMatTA',
                  'QteProdPeriodTA', 'QteProdTypeTA', 'TauxTransformArtisan']
