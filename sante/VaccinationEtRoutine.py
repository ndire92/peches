from django.forms import ModelForm
from sante.models import VaccinationEtRoutine
from django import forms


class vacin(ModelForm):
    CodeDistrict = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDeCouvertureAuPenta3 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDeCouvertureAuRR1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    TauxDeCouvertureAuHepBInferieurOuEgal24heures = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    Total0A11MoisNbreEnfantCompletementVaccine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    RR2Couverture12A23Mois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    Total12A23MoisFémininNbreEnfantCompletementVaccine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    Total12A23MoisMasculinNbreEnfantCompletementVaccine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = VaccinationEtRoutine
        fields = "__all__"
