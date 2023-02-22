from django.forms import ModelForm
from peche.models import DimPecheArtisan
from django import forms


class DPA(ModelForm):

    ActPech_Artisan = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    GroupPecheur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    GroupMareyeur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypePirogu = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogBois = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogFibr = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypProdPechPirogAlumin = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuHiver = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuInterSaison = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuSaisFroid = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeProdHalieuPrimptem = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    IntrantPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    MatUtilisePech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovis_Intran = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovis_Materiel = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenHiver = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenInterSaison = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenSaisFroid = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenPrintem = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivCaptMoyenSortTypProd = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptHiver = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptInterSaison = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptSaisFroid = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptPrintem = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NivPertPostCaptTypProd = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPecheArtisan
        fields = ['ActPech_Artisan', 'GroupPecheur', 'GroupMareyeur', 'TypePirogu', 'TypProdPechPirogBois',
                  'TypProdPechPirogFibr', 'TypProdPechPirogAlumin', 'TypeProdHalieuHiver', 'TypeProdHalieuInterSaison',
                  'TypeProdHalieuPrimptem', 'IntrantPech', 'MatUtilisePech', 'SourcApprovis_Intran', 'SourcApprovis_Materiel',
                  'NivCaptMoyenHiver', 'NivCaptMoyenInterSaison', 'NivCaptMoyenSaisFroid', 'NivCaptMoyenPrintem', 'NivCaptMoyenSortTypProd',
                  'NivPertPostCaptHiver', 'NivPertPostCaptInterSaison', 'NivPertPostCaptSaisFroid', 'NivPertPostCaptPrintem', 'NivPertPostCaptTypProd'
                  ]
