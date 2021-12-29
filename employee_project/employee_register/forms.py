from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
     
     class Meta:
         model = Employee
         fields = ('fullname','emp_code','mobile','position')
         labels = {
             'fullname' : 'Full Name',
             'emp_code' : 'Employee Code',
             'mobile' : 'Mobile Number',
             'position' : 'Position',
         }