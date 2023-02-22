from django.forms import ModelForm
from education.models import DimEduc_Perfomance
from django import forms


class DPRF(ModelForm):

    PerNombreNouveauxInscritsCPAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsCPAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCiAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsCE1AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsCE2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsCM1AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsCM2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsCE1AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsCE2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsCM1AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsCM2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCpAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCE1AnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCE2AnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCM1AnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombleElevesCM2AnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits5emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits4emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits3emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits1ereAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsTerminaleAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsEn5emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsEn4emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsEn3emeAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsEn1erAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreRedoublantsTerminaleAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreEleves6emeAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreEleves5emeAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreEleves4emeAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreEleves2ndeAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreEleves1erAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrisGarconsCM2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsFillesCM2AnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerPopulationJeunesAge11ansAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits3emeGarconsAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscrits3emeFillesAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerPopulationJeunesAge15ansAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxInscrits6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxFillesInscrits6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxGarconsInscrits6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerEffectifTotalInscritCm2AnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxInscrit2ndAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxGarconsInscrits2nd = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNouveauxFillesInscrits2nd = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerEffectifTotalInscrit3emeAnneeT_1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreNouveauxInscritsEnTerminaleAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreFillesNouveauxInscritsTerminale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerNombreGarconsNouveauxInscritTerminale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerPopulationJeunesAges18ansAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerPopulationJeunesGarçonsAge18ansAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerPopulationJeunesFilles18ansAnneeT = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatCFEE = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatCFEE_Filles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatCFEE_Garcons = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBFEM = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBFEM_Filles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBfem_Garcons = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBac = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBac_Filles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PerResultatBac_Garcons = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Perfomance

        fields = "__all__"
