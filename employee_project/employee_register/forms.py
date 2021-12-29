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
             'position' : 'Position'
         }

     def __init__(self, *args, **kwargs):
         super(EmployeeForm,self).__init__(*args, **kwargs)
         self.fields['position'].empty_label = "Select"
        