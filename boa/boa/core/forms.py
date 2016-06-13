from django import forms
from boa.core.models import Answer


class AnswerForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={"class":"input__field input__field--hoshi",
                                      "id":"nameinput",
                                      "name":"name",
                                      "data-role":"none",}
                           ))
    question = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={"class":"input__field input__field--hoshi",
                                          "id":"questioninput",
                                          "name":"question",
                                          "data-role":"none",}
                               ))
