from django.forms import ModelForm


from django import forms

from peche.models import DimPecheTAInnovat


class pectaino(ModelForm):
    codeCommune= forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
   
    TechnoIntroTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TechnoAdoptTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CausNoAdoptTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CausTechnoNoAdopTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    
    class Meta:
        model = DimPecheTAInnovat
        fields = ['codeCommune','nomCommune','TechnoIntroTA', 'TechnoAdoptTA',
                  'CausNoAdoptTA', 'CausTechnoNoAdopTA','date','date_modification']
