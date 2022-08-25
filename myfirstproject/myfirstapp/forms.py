import email
from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Tittle',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='subject',max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))

