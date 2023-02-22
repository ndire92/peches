from django.forms import ModelForm
from sante.models import SantePaludisme
from django import forms


class santePalu(ModelForm):
    CodeDistrict = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDeMorbiditeProportionnellePalustreTousAge = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDeMorbiditeProportionnellePalustreChezLesFemmesEnceintes = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDemorbiditeProportionnellePalustreChezLesMoinsDe5ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    IND20IncidenceDuPaludismePour1000Habitants = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    IncidenceDuPaludismegGraveTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20CasPaludismeConfirmesTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    ombreTotalDeCasPaludismeSimpleConfirmesEnregistreesSurLaPériodeParLesDSDOMQuiOntReçuUnTraitemen = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = SantePaludisme
        fields = "__all__"
