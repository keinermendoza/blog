from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    