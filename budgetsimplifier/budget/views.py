from . import utils
from datetime import date, timedelta
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from .models import PayConfiguration, Expense
from budgetsimplifier.users.models import User
from .forms import ExpenseForm, SimpleTestForm
from .tables import ExpenseTable


@method_decorator(login_required(login_url='home'), name='dispatch')
class BudgetMainView(TemplateView):
    template_name='components/home.html'
    def get(self, request):
        latest_pay_configuration = PayConfiguration.objects.filter(owner=request.user).order_by('-date_active_from')[0]
        previous_pay = utils.get_previous_pay_date(latest_pay_configuration.date_active_from, date.today(), 14)
        next_pay = previous_pay + timedelta(days=14)
        context = {
            'latest_pay_configuration':latest_pay_configuration,
            'pay_cycles_this_month': utils.fortnightly_cycles_current_month(latest_pay_configuration.date_active_from),
            'previous_pay': previous_pay,
            'next_pay': next_pay,
            'rolling_pays': utils.get_rolling_nine_pay_dates(latest_pay_configuration.date_active_from, date.today(), 14),
            }
        return render(request, self.template_name,context)

@method_decorator(login_required(login_url='home'), name='dispatch')
class ExpenseListMainView(TemplateView):
    template_name='components/expense.html'
    form_class = ExpenseForm
    
    def get(self, request):
        print(self.kwargs)
        form = ExpenseForm()
        expenses = ExpenseTable(Expense.objects.filter(owner=request.user))
        context = {
            'expenses': expenses,
            'form': form,
            'expense_table': expenses,
            }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='home'), name='dispatch')
class ExpenseFormNew(TemplateView):
    template_name='components/expenseView.html'
    
    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
        return redirect('budget:expenses')


    def get(self, request):
        form = ExpenseForm()
        context = {
            'form': form,
            'title': 'Create Expense',
            'action': request.get_full_path,
        }
        return render(request, self.template_name, context)
    
@method_decorator(login_required(login_url='home'), name='dispatch')
class DeleteExpense(TemplateView):
    def get(self, request, pk):
        Expense.objects.filter(pk=pk).delete()
        return redirect('budget:expenses')
        
@method_decorator(login_required(login_url='home'), name='dispatch')
class ExpenseFormUpdate(TemplateView):
    template_name='components/expenseView.html'
    def get(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        form = ExpenseForm(instance=expense)
        context = {
            'form': form,
            'title': 'Update Expense',
            'action': request.get_full_path,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        form = ExpenseForm(request.POST, instance = expense)
        form.save()
        return redirect('budget:expenses')
