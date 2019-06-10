from django.conf.urls import url
from django.urls import path, re_path

from django.views.generic import TemplateView
from django.views import defaults as default_views

from . import views
from . import views_api

app_name="budget"

urlpatterns = [
    path('', views.BudgetMainView.as_view(), name='home'),
    re_path('api/budget_list/(?P<user_id>[0-9a-f-]+)/$', views_api.get_budgets, name='budget_list_api'),
    path('expenses/', views.ExpenseListMainView.as_view(), name='expenses'),
    path('expenses/<int:pk>/', views.ExpenseFormUpdate.as_view(), name='expense_action'),
    path('expenses/create/', views.ExpenseFormNew.as_view(), name='create_expense'),
    path('expenses/delete/<int:pk>/', views.DeleteExpense.as_view(), name='delete_expense'),
]
