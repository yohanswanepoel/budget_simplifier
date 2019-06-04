from django_tables2 import tables
from django_tables2.utils import A
from .models import Expense

class ExpenseTable(tables.Table):
    change = tables.columns.TemplateColumn('''<a href="{% url 'budgetsimplifier:expenses' %}{{ record.id }}">Update</a>
                                   <a href="{% url 'budgetsimplifier:expenses' %}delete/{{ record.id }}" 
                                   onclick="return confirm('Are you sure you want to delete this?')">Delete</a>''',
                                   verbose_name=u'Change', )
    class Meta:
        model = Expense
        fields = ['name','frequency','cost','day_of_month']
        row_attrs = {
            'onclick': "edit_record()",
            'data-id': lambda record: record.pk
        }