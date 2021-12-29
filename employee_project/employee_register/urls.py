from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form,name = 'employee_insert'), #get and post request for insert operation
    path('<int:id>/', views.employee_form, name = 'employee_update'), #get and post request for update operation
    path('list/',views.employee_list,name = 'employee_list'), #get and view all the list of employees
    path('delete/<int:id>/',views.employee_delete,name= 'employee_delete') #delete relevent employee 
]