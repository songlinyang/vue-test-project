from django import forms

class TaskForm(forms.Form):
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

class TaskInterfaceFrom(forms.Form):
    task_id = forms.IntegerField(required=True)
    interface_id = forms.IntegerField(required=True)