from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]

        widgets = {
            "body": forms.Textarea(attrs={"rows":4})
        }

        error_messages = {
            "name": {
                "required": "Por favor llene el campo Nombre",
                "max_length": "Este campo acepta hasta 120 caracteres"
            },
            "email": {
                "required": "Por favor ingrese su Email",
                "invalid": "Email invalido"
            },
            "body": {
                "required": "Estoy feliz de que quiera comentar, por favor rellene el campo Comentario",
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
    nombre = forms.CharField(max_length=120)
    correo = forms.EmailField()
    destinatario = forms.EmailField()
    comentario = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4}))

    class Meta:
        invalid_message = "Email invalido"

        error_messages = {
            "name": {
                "required": "Por favor llene el campo Nombre",
                "max_length": "Este campo acepta hasta 120 caracteres"
            },
            "email": {
                "required": "El campo Correo es necesario",
                "invalid": invalid_message,
            },
            "to": {
                "required": "El campo Destinatario es necesario",
                "invalid": invalid_message,
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs = {
        #         'id': f"id_{field}_share"
        #     }
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    