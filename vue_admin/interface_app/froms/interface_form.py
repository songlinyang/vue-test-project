from django import forms


class InterfaceForm(forms.Form):
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
    service_id = forms.IntegerField(
        required=True
    )
    context = forms.CharField(
        min_length=1,
        max_length=5000,
        required=True
    )
