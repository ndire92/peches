from django.forms import ModelForm
from das.models import MultiStepFormModel
from django import forms


class MultiForm(ModelForm):

    fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    lname  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    phone  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    twitter  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    gplus  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    email  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    password  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = MultiStepFormModel
        fields = ['fname', 'lname', 'phone','twitter','facebook','gplus','email','password']