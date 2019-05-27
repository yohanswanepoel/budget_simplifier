from django.contrib import admin
from .models import Budget, PayConfiguration

admin.site.register(Budget)  # Register Accounts for administration, useful for development
admin.site.register(PayConfiguration)

