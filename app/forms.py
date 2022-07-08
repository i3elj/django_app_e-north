from django import forms
from django.forms import ModelForm

from app.models import *

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = [
            'subject',
            'grade_one',
            'grade_two',
            'grade_three',
        ]
