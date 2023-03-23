from django.forms import ModelForm
from peche.models import DimPecheArtisan
from django import forms


class DPA(ModelForm):
    


    codeCommune = forms.CharField(label='code Commune', widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField( label='nom Commune',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ActPech_Artisan= forms.CharField( label='Acteur Peche Artisanale',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrActeur = forms.CharField(label='Nombre Acteur Peche',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    GroupPecheur= forms.CharField(label='Groupement Pecheur',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGIEPecheur = forms.CharField(label='Nbr GIE Pecheur',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrOrganiProfessPecheur = forms.CharField(label='Nbr Organisation Profess Pecheur',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbr_AssociatPecheur = forms.CharField(label='Nbr Association Pecheur',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    GroupMareyeur= forms.CharField(label='Groupement Mareyeur',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGIEMarey = forms.CharField(label='Nbre GIE Mareyeur ',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrOrganiProfessMarey = forms.CharField(label='Nbr Organisation Profess Mareyeur',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbr_AssociatMarey = forms.CharField(label='Nbr Association Mareyeur',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreQuaiPech = forms.CharField(label='Nbre Quai Pecheur ',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypePirogu= forms.CharField(label='Type Pirogue',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogBois= forms.CharField(label='Type Prod Peche Pirogue Bois',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogFibr= forms.CharField(label='Type Prod Peche Pirogue Fibre',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogAlumin= forms.CharField(label='Type Prod Peche Pirogue Alumine',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuHiver= forms.CharField(label='Type Prod Halieu Hiver ',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    
    TypeProdHalieuInterSaison= forms.CharField(label='Type de produits halieutiques en InterSaison:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuSaisFroid= forms.CharField(label='Type de produits halieutiques en Saison froide:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuPrimptem= forms.CharField(label='Type de produits halieutiques en Primptemps:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IntrantPech= forms.CharField(label='Intrants Peche:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    MatUtilisePech= forms.CharField(label='Matériels utilisés',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovis_Intran= forms.CharField(label='Sources d’approvisionnement en intrants',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovis_Materiel= forms.CharField(label='Sources d’approvisionnement en matériels:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Qteannuel_debarq = forms.CharField(label='Quantité annuel debarqué',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenHiver= forms.CharField(label='Niveau de capture moyenne par sortie en période Hivernage (saison chaude):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenInterSaison= forms.CharField(label='Niveau de capture moyenne par sortie en période Inter-saison (Looly):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenSaisFroid= forms.CharField(label='Niveau de capture moyenne par sortie en période Saison froide (Nör):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenPrintem= forms.CharField(label='Niveau de capture moyenne par sortie en période Printemps (Thiorone-inter-saison):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenSortTypProd= forms.CharField(label='Niveau de pertes post capture - (par période) en Hivernage (saison chaude):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptHiver= forms.CharField(label='Niveau de pertes post capture - (par période) en Inter-saison (Looly):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptInterSaison= forms.CharField(label=' Niveau de pertes post capture - (par période) en Inter-saison (Looly):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptSaisFroid= forms.CharField(label='Niveau de pertes post capture - (par période) en Saison froide (Nör):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptPrintem= forms.CharField(label='Niveau de pertes post capture - (par période) en Printemps (Thiorone-inter-saison):',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptTypProd= forms.CharField(label='Niveau de pertes post capture par type de produit:',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(label='date enrégistré',widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(label='date modification',widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    

    class Meta:
        model = DimPecheArtisan
        fields = ['codeCommune',
                        'nomCommune',
                        'ActPech_Artisan',
                        'NbrActeur',
                        'GroupPecheur',
                        'NbreGIEPecheur',
                        'NbrOrganiProfessPecheur',
                        'Nbr_AssociatPecheur',
                        'GroupMareyeur',
                        'NbreGIEMarey',
                        'NbrOrganiProfessMarey',
                        'Nbr_AssociatMarey',
                        'NbreQuaiPech',
                        'TypePirogu',
                        'TypProdPechPirogBois',
                        'TypProdPechPirogFibr',
                        'TypProdPechPirogAlumin',
                        'TypeProdHalieuHiver',

                        'TypeProdHalieuInterSaison',
                        'TypeProdHalieuSaisFroid',
                        'TypeProdHalieuPrimptem',
                        'IntrantPech',
                        'MatUtilisePech',
                        'SourcApprovis_Intran',
                        'SourcApprovis_Materiel',
                        'Qteannuel_debarq',
                        'NivCaptMoyenHiver',
                        'NivCaptMoyenInterSaison',
                        'NivCaptMoyenSaisFroid',
                        'NivCaptMoyenPrintem',
                        'NivCaptMoyenSortTypProd',
                        'NivPertPostCaptHiver',
                        'NivPertPostCaptInterSaison',
                        'NivPertPostCaptSaisFroid',
                        'NivPertPostCaptPrintem',
                        'NivPertPostCaptTypProd','date','date_modification' ]
