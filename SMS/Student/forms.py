from django import forms
forms.ModelForm
from .models import StudentModel


class StudentForm(forms.Form):
    rn = forms.IntegerField(label="Roll Number:")
    fnm = forms.CharField(max_length=30,label="First Name:")
    lnm = forms.CharField(max_length=30,label="Last Name:")
    mk = forms.FloatField(label="Marks:")

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'


    
    