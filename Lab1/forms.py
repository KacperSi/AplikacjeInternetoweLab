from django import forms

class prescriptionForm(forms.Form):
    number = forms.CharField(required=False)
    firstname = forms.CharField(required=False)
    surname = forms.CharField(required=False)