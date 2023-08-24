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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":4}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    