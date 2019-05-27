from django.http import JsonResponse
from .services import refresh_budgets

def get_budgets(request,user_id):
    return JsonResponse(refresh_budgets(user_id))
