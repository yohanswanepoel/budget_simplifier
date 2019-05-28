from . import utils
from datetime import date
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import PayConfiguration
from budgetsimplifier.users.models import User


@method_decorator(login_required(login_url='home'), name='dispatch')
class BudgetMainView(TemplateView):
    template_name='components/home.html'
    def get(self, request):
        latest_pay_configuration = PayConfiguration.objects.filter(owner=request.user).order_by('-date_active_from')[0]
        print(latest_pay_configuration)
        context = {
            'latest_pay_configuration':latest_pay_configuration,
            'pay_cycles_this_month': utils.fortnightly_cycles_current_month(latest_pay_configuration.date_active_from),
            'rolling_pays': utils.get_rolling_nine_pay_dates(latest_pay_configuration.date_active_from, date.today(), 14)
            }
        return render(request, self.template_name,context)
