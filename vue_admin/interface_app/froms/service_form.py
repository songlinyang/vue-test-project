from django import forms

class ServiceForm(forms.Form):
    name = forms.CharField(
        min_length=1,
        max_length=200,
        required=True
    )
    description = forms.CharField(
        min_length=1,
        max_length=2000,
        required=True
    )
    