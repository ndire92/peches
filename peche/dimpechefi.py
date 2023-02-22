from django.forms import ModelForm
from peche.models import DimPecheFinance
from django import forms


class DPFI(ModelForm):

    OffrServicFinancPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DemandApportPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypGaranExige = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LongProcedCredi = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauInteret = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DelaiRemboursMinMax = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPecheFinance
        fields = ['OffrServicFinancPech', 'DemandApportPech', 'TypGaranExige',
                  'LongProcedCredi', 'TauInteret', 'DelaiRemboursMinMax']
