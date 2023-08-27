from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        required_message = "Este campo es obligatorio"

        model = Comment
        fields = ["name", "email", "body"]

        widgets = {
            "body": forms.Textarea(attrs={"rows":4})
        }
        error_messages = {
            "name": {
                "required": required_message,
                "max_length": "Este campo acepta hasta 120 caracteres"
            },
            "email": {
                "required": required_message,
                "invalid": "Email invalido"
            },
            "body": {
                "required": required_message,
            }
        }
        help_texts = {
            "email": "El email se mantendrá en privado",
        }

        labels = {
            "name": "Nombre",
            "email": "Email",
            "body": "Comentario",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4}))

    class Meta:
        required_message = "Este campo es obligatorio"
        invalid_message = "Email invalido"

        error_messages = {
            "name": {
                "required": required_message,
                "max_length": "Este campo acepta hasta 120 caracteres"
            },
            "email": {
                "required": required_message,
                "invalid": invalid_message,
            },
            "to": {
                "required": required_message,
                "invalid": invalid_message,
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    