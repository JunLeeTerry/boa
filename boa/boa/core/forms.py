from django import forms
from boa.core.models import Answer


class AnswerForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={"class":"form-control",
                                      "name":"name"}
                           ))
    question = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={"class":"form-control",
                                          "name":"question"}
                               ))
