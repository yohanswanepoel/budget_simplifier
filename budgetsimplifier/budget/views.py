from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

@method_decorator(login_required(login_url='home'), name='dispatch')
class BudgetMainView(TemplateView):
    template_name='listbudgets.html'
    def get(self, request):
        context = {}
        return render(request, self.template_name,context)
