from django.forms import ModelForm
from sante.models import PlanificationFamiliale
from django import forms


class PLANFF(ModelForm):
    CodeDistrict = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20TauxdeRecrutementPF = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20TauxdAbandonPF = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20TotalAbandonsPF = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20PourcentagedeFemmesde15a49ansSousMethodeContraceptiveapresAvortement = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20PourcentagedUtilisatricesPF = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20PourcentagedUtilisatricesPFchezles15a49ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    R20TauxdePrevalencecontraceptive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    class Meta:
        model = PlanificationFamiliale
        fields = "__all__"
