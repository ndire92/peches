from django.forms import ModelForm
from sante.models import SurvieEnfant
from django import forms


class survienf(ModelForm):

    CodeDistrict = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    PourcentageEnfants0a59MoisAyantFaitUneDiarrhe = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20ProportionDeCasDePneuMonie0a59Mois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20ProportionEnfantsAvecPneumonieGraveDontLaSaturationEnoxygèneAEtemesuree = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20ProportionEnfantsDe0a59MoisSouffrantAnemie = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20ProportionEnfantsDe0a59moisPresentantUneAnemie = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    SAVEDeCasEnfantsDeMoinsDe5ansCorrectementSoignesContreLaDiarrheeDansLesCentresDeSanteCommunautairesM = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    NombreDeCasDeDiarrheeReferesParleNiveauCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageEnfantsDe6a11MoisSupplementesEnVitamineAEnRoutine = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageEnfantsDe12a59MoisSupplementesEnVitamineAEnRoutine = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageEnfantsDe12a59MoisDeParasitésEnRoutine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20ProportionEnfantsDe0a59MoisAyantUnNuméroEtatcivil = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20EnfantsDe0a59MoisReçusPourTraumatismeDuSaUnAccidentEtOuAUnActedeViolenceNombreTotalEnfants0a59MoisVusenConsultation = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    DiarrheeReferesParleNiveauCommunautaire0a59mois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    SupplementationSystematiqueEnVitamineADesEnfantsDe6a59Mois = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageEnfantsDe6a59MoisSupplementesEnVitamineAEnRoutine = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    PourcentageEnfants12a59MoisDeparasitesEnRoutineOK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20NombreDeCasDePneumonies0a59mois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGraveAvechypoxietraiteeParoxygénoThérapieAuNiveauDesPPSFeminin = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20NombreEnFantsDe0a59MoisPresentantUnePneumonieGraveAvecHypoxieTraiteeParoxygénoThérapieAuNiveauDesPPSMasculin = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGravecHezquilaSaturationEnOxygèneAEteMesureeAuNiveauDesPPSFeminin = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGravecHezquiLaSaturationEnOxygèneAEteMesureeAuNiveauDesPPSMasculin = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    R20PourcentageEnfantsde0a59MoisPresentantUnePneumonieGravechezquiLaSaturationEnOxygèneAEteMesureeAuNiveauDesPPS = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = SurvieEnfant
        fields = "__all__"
