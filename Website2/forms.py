from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","mail","body"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "mail": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }



