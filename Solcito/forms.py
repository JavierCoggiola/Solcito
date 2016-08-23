 # -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Solcito.models import Registration, Student, Tutor
from django.forms.utils import ErrorList
from material import *

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
