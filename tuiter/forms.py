from django import forms
from .models import Tuit


class TuitModelForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        label="",  # quito el label de 'body'
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "¿Que estas pensando ?",
                "class": "textarea is-success is-medium",
            }
        ),
    )

    class Meta:
        model = Tuit
        exclude = ("user", )
