from django.forms import ModelForm
from das.models import DimAgroProduction
from django import forms


class DimAgroprd(ModelForm):

    name_Production = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CodeCulture = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    type_cult_prat = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    RendemHectarCult = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauxPertPostRecoltParCult = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeSolExist = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeDegradZonCultur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CauseDegrad = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimAgroProduction
        fields = ['name_Production', 'CodeCulture', 'type_cult_prat', 'RendemHectarCult',
                  'TauxPertPostRecoltParCult', 'TypeSolExist', 'TypeDegradZonCultur', 'CauseDegrad']
