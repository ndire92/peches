from django.forms import ModelForm
from education.models import DimEduc_Personnel
from django import forms


class DPR(ModelForm):

    PersEnseignantsPrescolairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrescolairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrescolaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantPrescolaieTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrescolairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrescolairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrescolaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrescolaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreStructurePrescolaireDisposantInfirmerie = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrimairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrimairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrimaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrimaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrimairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrimairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesPrimaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreClassesUnSeulMaitreDonneCours2cohortesPrimaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreClassesDansLesquellesUnseulEnseignantEstChargeDePlusieursNiveauxPrimaire = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEcolePrimairesPubliquesDisposantAuMoinsUnInfirmierScolaire = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEcolePrimairesPriveesDisposantAuMoinsUnInfirmierScolaire = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEcolePrimairesCommunautairesDisposantAuMoinsUnInfirmierScolaire = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantDiplomeProfessionnelCAP = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantDiplômeCEAP = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireSansDiplomeProfessionnel = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantBac = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantBFEM = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantCFEE = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantBacplus2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantLicence = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsduPrimaireAyantDiplomeMaitriseMasterDEA = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPrimaireAyantAutresDiplome = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignants6emeA3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignantsHommes6emeA3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignantsFemmes6emeA3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicCollegeSelonDiplomeProfessionnelCAECEM = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicCollegeSelonDiplomeProfessionnelCAES = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicCollegeSansDiplomeProfessionnel = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesTotalMoyenGeneral6emeA3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesGarconsMoyenGeneral6A3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesFillesMoyenGeneral6emeA3eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersPersonnelAdministratifMoyenSecondaireHomme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersPersonnelAdministratifMoyenSecondairFemme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersPersonnelAdministratifMoyenSecondaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsLyceePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantLyceePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsTotalLycee = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesTotalSecondaireGeneral2nd_Tle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesGarconsSecondaireGeneral2nd_Tle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersElevesFillesSecondaireGeneral2nd_Tle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignantsTotal2nd_Tle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignantsHommes2nd_Tle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreEnseignantsFilles2nd_Tles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreMedecinEtablissementPulicSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreMedecinEtablissementPriveSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersNombreMedecinSecondaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicSecondaireAyantDiplomeAcademieBAC = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicSecondaireAyantDiplomeAcademieBFEM = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantPublicSecondaireAyantDiplomeAcademieCFEE = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsDuPublicSecondaireAyantBasplus2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicSecondaireAyantLicence = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicSecondaireAyantDiplomeMaitrise_MasterPlus = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '    ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersEnseignantsPublicSecondaireAyantAutresDiplomeAcademique = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Personnel
        fields = "__all__"
