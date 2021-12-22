from django import forms
from django.contrib.auth.models import User
from testapp.models import *
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','first_name','username','password']
class NewAccountForm(forms.ModelForm):
    class Meta:
        model=NewAccount
        fields='__all__'
class NewExpenseForm(forms.ModelForm):
    class Meta:
        model=NewExpense
        fields='__all__'
class NewDepartForm(forms.ModelForm):
    class Meta:
        model=NewDepart
        fields='__all__'
class ItemExpenseForm(forms.ModelForm):
    class Meta:
        model=ItemExpense
        fields='__all__'
class HrExpenseForm(forms.ModelForm):
    class Meta:
        model=HrExpense
        fields='__all__'
class MiscExpensesForm(forms.ModelForm):
    class Meta:
        model=MiscExpenses
        fields='__all__'
class GenerateReportForm(forms.ModelForm):
    class Meta:
        model=GenerateReport
        fields='__all__'
