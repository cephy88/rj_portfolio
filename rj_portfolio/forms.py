from django import forms


class MyForm(forms.Form):
    a = forms.CharField(max_length=20)