from django import forms
from Solcito.models import Registration, Student, Tutor
from django.forms.utils import ErrorList

class EditRegistrationForm(forms.ModelForm):

    error_css_class = 'alert alert-danger'

    class Meta:

        model = Student
        exclude = ('idStudent', 'photo')


    def __init__(self, *args, **kwargs):
        super(EditRegistrationForm, self).__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['placeholder'] = 'Requerido'
                field.label = '* ' + field.label
