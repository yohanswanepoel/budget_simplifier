from django.conf.urls import url

from django.views.generic import TemplateView
from django.views import defaults as default_views

from . import views
from . import views_api

app_name="budget"

urlpatterns = [
    url(r'^$', views.BudgetMainView.as_view(), name='home'),
    url(r'^api/budget_list/(?P<user_id>[0-9a-f-]+)/$', views_api.get_budgets, name='budget_list_api')
]
