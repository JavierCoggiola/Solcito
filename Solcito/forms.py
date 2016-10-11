 # -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Solcito.models import RegistrationS, Student, Tutor, Teacher
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms.utils import ErrorList
from material import *



class RegistrationSForm(ModelForm):

    layout = Layout(
        Row(Span6('activeDate')),Span6('desactiveDate'),
        Row(Span12('student')),
        Row(Span12('curso')),
    )
    class Meta:
        model = RegistrationS
        exclude = ('idRegistrationS',)

class TeacherForm(ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.CharField(
        label=_("username"),
        strip=False,
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = Teacher
        exclude = ('idteacher',)

    def clean(self):
        '''
        Check forms errors
        '''
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password1', 'Please, input the same password')
            self.add_error('password2', 'Please, input the same password')

        try:
            u = User.objects.get(username=cleaned_data.get("username"))
            self.add_error('username', 'This username is alredy in use')
        except:
            pass

    def save(self, commit=True):
        #Create user
        cleaned_data = self.cleaned_data
        user = User(username=cleaned_data.get("username"),
                    is_staff=True)

        user.set_password(cleaned_data["password1"])
        user.save()
        if cleaned_data['tipo'] == "teacher":
            group = Group.objects.get(name='Docente')
            user.groups.add(group)
        elif cleaned_data['tipo'] == "celador":
            group = Group.objects.get(name='Preceptor')
            user.groups.add(group)
        #create teacher
        try:
            instance = super(TeacherForm, self).save(commit=False)
            instance.authuser = user
            if commit:
                instance.save()
        except:
            user.delete()
        return instance

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



class StudentForm(ModelForm):

    layout = Layout(
        Row(Span6('name'), Span6('lastName')),
        Row(Span6('email'),Span3('dni'), Span3('sex')),
        Row(Span4('landline'), Span4('cellphone'),Span4('birthDate')),
        Row('religion', 'birthPlace', 'nacionality'),
        Row(Span5('street'), Span5('neighborhood'), Span2('numberStreet')),
        Row(Span3('PC'), Span3('tower'), Span3('floorDepartment'), Span3('department')),
    )

    class Meta:
        model = Student
        exclude = ('idStudent', 'photo')

    def clean(self):
        cleaned_data = self.cleaned_data
        print (cleaned_data)
        try:
            birthDate = cleaned_data.get("birthDate")
        except:
            birthDate = None
        if not birthDate:
            self.add_error('birthDate', 'Este campo es obligatorio')
        try:
            landline = cleaned_data.get("landline")
        except:
            pass

        try:
            cellphone = cleaned_data.get("cellphone")
        except:
            pass

        if landline != None:
            lenphone = len(str(landline))
        else:
            lenphone = 0
        if cellphone != None:
            len_cell = len(str(cellphone))
        else:
            len_cell = 0
        if lenphone < 7 and len_cell < 7 :
            msg = "Por favor, ingrese al menos un número telefónico válido."
            self.add_error('landline', msg)
            self.add_error('cellphone', msg)


class GuardianForm(ModelForm):
    layout = Layout(
        Row(Span6('name'), Span6('lastName')),
        Row(Span4('email'), Span4('dni'), Span4('cuil')),
        Row('locality' , 'nacionality'),
        Row(Span4('landline'), Span4('cellphone'), Span4('workPhone')),
        Row(Span6('profession'), Span6('workPlace')),
        Row(Span5('street'), Span5('neighborhood'), Span2('numberStreet')),
        Row(Span3('PC'), Span3('tower'), Span3('floorDepartment'), Span3('department')),
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        print (cleaned_data)
        try:
            landline = cleaned_data.get("landline")
        except:
            pass

        try:
            cellphone = cleaned_data.get("cellphone")
        except:
            pass

        if landline != None:
            lenphone = len(str(landline))
        else:
            lenphone = 0
        if cellphone != None:
            len_cell = len(str(cellphone))
        else:
            len_cell = 0
        if lenphone < 7 and len_cell < 7 :
            msg = "Por favor, ingrese al menos un número telefónico válido."
            self.add_error('landline', msg)
            self.add_error('cellphone', msg)

    class Meta:
        model = Tutor
        exclude = ('students','rol')
