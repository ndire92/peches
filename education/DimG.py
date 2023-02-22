from django.forms import ModelForm
from education.models import DimEduc_Gouvernance
from django import forms


class Dg(ModelForm):

    DepensesInvestissement = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    MasseSalariale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    PersonnelAppui = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    MasseSalarialeDuPersonnelEnChage = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DepenseEnEau = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DepenseEnElectricite = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    AchatDeFournitureScolaireAideSociale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    BeneficiaireDesActivitesRenforcementDeCapaciteEtFormationProfessionnel = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DepensesPourLeRenforcementDeCapaciteFormationProfessionnelle = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DepensesPourHebergementDesEtudiants = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    NombreDeRecompenses = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    NombreDeBourses = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    MontantDesRecompenses = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    MontantDesBources = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    TotalDesDepensesEnEducation = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    DepensesInvestissementDansEducation = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    MasseSalarialeFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    MasseSalarialeDuPersonnelEnChageFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    AchatDeFournitureScolaireAideSocialeFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'})),
    DepensesPourLeRenforcementDeCapaciteFormationProfessionnelleFloat = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    DepensesPourHebergementDesEtudiantsFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    MontantDesRecompensesFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    MontantDesBourcesFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    TotalDesDepensesEnEducationFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'})),
    DepensesInvestissementDansEducationFloat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Gouvernance
        fields = "__all__"
