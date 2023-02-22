from django.forms import ModelForm
from peche.models import DimPechTAFinance
from django import forms


class pectafina(ModelForm):

    OffrServicFinancTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DemandApportTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypGaranExigeTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LongProcedCrditTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauInterTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DelaiRemboursMinMaxTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimPechTAFinance
        fields = ['OffrServicFinancTA', 'DemandApportTA', 'TypGaranExigeTA',
                  'LongProcedCrditTA', 'TauInterTA', 'DelaiRemboursMinMaxTA']
