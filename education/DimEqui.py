from django.forms import ModelForm
from education.models import DimEduc_Equipements
from django import forms


class equi(ModelForm):
    EquiNombreCasesDesTouPetits = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreGarderie = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreMaternelle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    NombrePrescolaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructurePrescolaireDisposantCantinesScolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClasseAvecUnLocalNormalPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClasseSituationAbrisProvisoirePrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructurePrescolaireDisposantDeCloturePrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructurePrescolairesDisposantElectricitePrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreTotalLatrinesFonctionnellesPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesGarconsPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesFillesPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePontsEauCourantePrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEnfantsBeneficieDeparasitageMTN_Prescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEnfantsBeneficieDeparasitageFER_Prescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructureElementaireDisposantCantinesScolaires = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClassePrimaireAvecUnLocalNormal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClassePrimaireEnSituationAbrisProvisoire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructureElementaireDisposantCloture = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiTotalLatrinesFonctionnellesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesGarconsPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesFillesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolePubliquesAyantElectricitePrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEauCourantePrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructutesPubliquesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructurePriveesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePubliquePrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePubliquePrivees = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClasseAvecUnLocalNormalPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClassePrimaireEnSituationAbrisProvisoirePrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalEtablissementPrimairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreGroupePedagogiquesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreClassesPhysiquesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolesEquipeeSalleInformatiquePrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolesPrimaireDisposantConnexionInternet = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructureDisposantCatineScolaireMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClasseAvecLocalNormalMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClasseSituationAbrisProvisoireMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructuresElementaireDisposantClotureMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiTotalLatrinesFonctionnellesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesGarconsMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFonctionnellesFillesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolesPubliquesAyantElectriciteMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEauCouranteMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructurePubliquesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructurePriveesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePubliquesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePriveesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClasseAvecUnLocalNormalMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreGroupePedagogiquesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreClassesPhysiquesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolesEquipeeSalleInformatiqueMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcoleDisposantConnexionInternetMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructureDisposantCatineScolaireSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClasseAvecUnLocalNormalSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesClasseSituationAbrisProvisoireSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreStructuresSecondaireDisposantCloture = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiTotalLatrinesFonctionnellesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesGarconsFonctionnellesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiLatrinesFillesFonctionellesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcolePubliquesAyantElectriciteSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEauCouranteSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructurePubliquesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombrePlacesAssisesStructutesPriveesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePubliquesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreElevesStructurePriveeSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesDeClasseAvecunLocalNormalSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreSallesTotalSecondairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreGroupesPedagogiquesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreClassePhysiquesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquiNombreEcoleEquipeeSalleInformatiqueSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    EquipementNombreEcoleDisposantConnexionInternetSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:

        model = DimEduc_Equipements
        fields = "__all__"
