
from django import forms
from app.models import Ressource


class Ressou(forms.ModelForm):
    title = forms.CharField(label='Title',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    mot_cle = forms.CharField(label=' mot clé',widget=forms.Textarea(attrs={'placeholder': ' ', 'style': 'width: 600px;', 'class': 'form-control'}))
    
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
   
    action =forms.FileField()
    
    
    class Meta:
        model = Ressource
        fields = ('title','mot_cle','date_en','action')