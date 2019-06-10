from django_tables2 import tables
from django_tables2.utils import A
from .models import Expense

class ExpenseTable(tables.Table):
    change = tables.columns.TemplateColumn('''<a class="btn" href="#" onclick="edit_expense({{ record.id }})">Edit</a>
                                              <a class="btn" href="#" onclick="delete_expense({{ record.id }})">Delete</a>''',
                                   verbose_name=u'Change', )
    class Meta:
        model = Expense
        fields = ['name','frequency','cost','day_of_month']
        row_attrs = {
            'data-id': lambda record: record.pk
        }