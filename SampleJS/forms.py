from django.forms import forms, fields


class RegistrationForm(forms.Form):
    username = fields.CharField(min_length=4, max_length=20)
    email = fields.EmailField()
    password = fields.CharField(min_length=6, max_length=20)


class StudentForm(forms.Form):
    age = fields.IntegerField(min_value=6, max_value=20)
