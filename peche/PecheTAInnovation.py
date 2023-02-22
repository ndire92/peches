from django.forms import ModelForm


from django import forms

from peche.models import DimPecheTAInnovat


class pectaino(ModelForm):

    TechnoIntroTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TechnoAdoptTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CausNoAdoptTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CausTechnoNoAdop = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPecheTAInnovat
        fields = ['TechnoIntroTA', 'TechnoAdoptTA',
                  'CausNoAdoptTA', 'CausTechnoNoAdop']
