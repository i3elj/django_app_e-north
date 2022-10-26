from django import forms
from django.forms import ModelForm

from app.models import Student, Grade


class StudentCreationForm(forms.Form, forms.ModelForm):
    """class StudentCreationForm(forms.Form, forms.ModelForm)"""
    born_at = forms.DateTimeField(
        label="Birthday:",
        input_formats=['%d/%m/%Y'],
        initial="30/12/1999"
    )

    class Meta:
        model = Student
        fields = '__all__'


class GradeForm(forms.ModelForm):
    """class GradeForm(forms.ModelForm)"""
    class Meta:
        model = Grade
        fields = [
            'subject',
            'grade_one',
            'grade_two',
            'grade_three',
            'grade_four',
        ]
