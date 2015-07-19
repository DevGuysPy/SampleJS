from django.forms import forms, fields


class RegistrationForm(forms.Form):
    username = fields.CharField(min_length=4, max_length=20)
    email = fields.EmailField()
    password = fields.CharField(min_length=6, max_length=20)

