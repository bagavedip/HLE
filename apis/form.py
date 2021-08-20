from django import forms


class ActionForm(forms.Form):
    url = forms.URLField()
