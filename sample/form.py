from django import forms


class ActionForm(forms.Form):
    file = forms.FileField()
