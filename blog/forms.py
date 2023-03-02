from django.urls import reverse_lazy
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

        widgets = {
            "body": forms.Textarea(attrs={"rows":4})
        }
        error_messages = {
            "body": {
                "required": "Estoy feliz de que quiera comentar, por favor rellene el campo Comentario",
            }
        }
        labels = {
            "body": "Comentario",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     
        self.helper = FormHelper(self)
        self.helper.form_tag = False


class EmailPostForm(forms.Form):
    destinatario = forms.EmailField(help_text="Enviaré su recomendación a este email")
    comentario = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4}))
                                 

    class Meta:
        error_messages = {
            "comentario": {
                "required": "Estoy feliz de que quiera recomendar mi publicación, por favor rellene el campo Comentario",
            },
            "destinatario": {
                "required": "El campo Destinatario es necesario",
                "invalid": "Email no valido",
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

class LoginForm(forms.Form):
    nombre = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"autofocus":"autofocus"}))
    contraseña = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"type":"password"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('login')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Iniciar Sesion', css_class="btn-outline-dark"))

class RegisterForm(LoginForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('register')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn-outline-dark"))