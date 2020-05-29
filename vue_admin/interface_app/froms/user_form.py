from django import forms


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        error_messages={
            "required":"用户名或密码不能为空"
        }
    )
    password = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        error_messages={
            "required":"用户名或密码不能为空，且最小密码长度为8位"
        }

    )