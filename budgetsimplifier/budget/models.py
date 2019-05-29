from django.db import models
from django.utils.translation import ugettext_lazy as _
from budgetsimplifier.users.models import User


class Budget(models.Model):
    number = models.CharField(verbose_name=_("Acc Number"), max_length=50)
    name = models.CharField(verbose_name=_("Acc Name"), max_length=50)
    display_name = models.CharField(verbose_name=_("Display Name"), max_length=50)
    balance = models.DecimalField(verbose_name=_("Balance"), max_digits=10, decimal_places=2)
    balance_date = models.DateTimeField(verbose_name=_("Date Updated"), auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=None, null=False, verbose_name=_("Owner"), related_name='%(class)s_owner')

    def __str__(self):
        return self.display_name

class Expense(models.Model):
    AT_PAY = 'AP'
    MONTHLY = 'MO'
    ADD_HOC = 'AH'
    QUARTERLY = 'QY'
    PAY_CYCLE_CHOICES = {
        (AT_PAY, 'At Pay'),
        (MONTHLY, 'Monthly'),
        (ADD_HOC, 'Add Hoc'),
        (QUARTERLY, 'Quarterly'),
    }
    name = models.CharField(verbose_name=_("Expense"), max_length=100)
    frequency = models.CharField(
        verbose_name = "Expense Frequency",
        max_length = 2,
        choices = PAY_CYCLE_CHOICES,
        default = AT_PAY
    )
    cost = models.DecimalField(verbose_name="Expense $",max_digits=12,decimal_places=2)
    day_of_month = models.IntegerField(verbose_name="Day of Month")

    def _str_(self):
        return self.name

class PayConfiguration(models.Model):
    FORTNIGHTLY = 'FN'
    WEEKLY = 'WY'
    MONTHLY = 'MO'
    ADD_HOC = 'AH'
    PAY_CYCLE_CHOICES = {
        (FORTNIGHTLY, 'Fortnightly'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (ADD_HOC, 'Add Hoc'),
    }
    frequency = models.CharField(
        verbose_name = "Payment Frequency",
        max_length = 2,
        choices = PAY_CYCLE_CHOICES,
        default = FORTNIGHTLY
    )
    take_home_pay = models.DecimalField(verbose_name="Take Home Pay", max_digits=12, decimal_places=2)
    date_active_from = models.DateField(verbose_name="Date Active From")
    owner = models.ForeignKey(User, on_delete=None, null=False, verbose_name=_("Owner"), related_name='%(class)s_owner')

    def __str__(self):
        return "%s %s %s" % (self.owner, str(self.date_active_from), self.frequency)