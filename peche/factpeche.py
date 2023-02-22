from django.forms import ModelForm

from django import forms

from peche.models import FactPeche


class factpeche(ModelForm):

    Temps_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechArtisan_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechAssure_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechComm_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechFinance_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechInnov_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechInnovTA_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechTAAssure_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechTAComm_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechTAFinance_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdPechTransFormArtisan_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdGeographie_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrActeur = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGIEPecheur = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrOrganiProfessPecheur = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbr_AssociatPecheur = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))

    NbreGIEMarey = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrOrganiProfessMarey = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbr_AssociatMarey = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreQuaiPech = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrPirogBois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePirogFibVer = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrPirogAlumin = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePirogImmatri = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSouscripPech = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePrimePech = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Qteannuel_debarq = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    PriVentMoy_Prod = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrSouscripTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrixVentMoyProdTA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = FactPeche
        fields = ['Temps_FK', 'IdPechArtisan_FK', 'IdPechAssure_FK', 'IdPechComm_FK', 'IdPechFinance_FK', 'IdPechInnov_FK', 'IdPechInnovTA_FK',
                  'IdPechTAAssure_FK', 'IdPechTAComm_FK', 'IdPechTAFinance_FK', 'IdPechTransFormArtisan_FK', 'IdGeographie_FK', 'NbrActeur',
                  'NbreGIEPecheur', 'NbrOrganiProfessPecheur', 'Nbr_AssociatPecheur', 'NbreGIEMarey', 'NbrOrganiProfessMarey', 'Nbr_AssociatMarey',
                  'NbreQuaiPech', 'NbrPirogBois', 'NbrePirogFibVer', 'NbrPirogAlumin', 'NbrePirogImmatri', 'NbreSouscripPech', 'NbrePrimePech', 'Qteannuel_debarq',
                                  'PriVentMoy_Prod', 'NbrSouscripTA', 'PrixVentMoyProdTA']
