from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name','frequency','cost','day_of_month']

class SimpleTestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)