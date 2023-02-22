from django.forms import ModelForm
from sante.models import ReproductionEtJeune
from django import forms


class reprojeu(ModelForm):

    CodeDistrict = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAdolescentes15a19anSousMethodeContraceptiveApresAvortement = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAdolescentes20a24ansSousMethodeContraceptiveApresAvortement = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageDAvortementsChezLesAdolescentesDe15a19ansPrisEnChargeParAmiuAuPremierTrimestre = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAvortementsChezLesJeunesFemmesDe20a24ansPrisEnChargeAuPremierTrimestreParMisoprostol = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAvortementsChezLesAdolescentesDe20a24ansPrisEnChargeParAmiuAuPremierTrimestre = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAvortementsChezLesAdolescentesDe15a19ansPrisEnChargeAuPremierTrimestreParMisoprostol = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAccouchementsDesAdolescentesDe15a19ansAssistesParUnPersonnelQalifie = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageAccouchementsDesAdolescentesDe20a24ansAssistesParUnPersonnelQualifie = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageUtilisatricesPFchezLes15a49ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = ReproductionEtJeune
        fields = "__all__"
