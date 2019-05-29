# Generated by Django 2.2.1 on 2019-05-29 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0002_auto_20190529_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=None, related_name='expense_owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='frequency',
            field=models.CharField(choices=[('AH', 'Add Hoc'), ('AP', 'At Pay'), ('QY', 'Quarterly'), ('MO', 'Monthly')], default='AP', max_length=2, verbose_name='Expense Frequency'),
        ),
        migrations.AlterField(
            model_name='payconfiguration',
            name='frequency',
            field=models.CharField(choices=[('AH', 'Add Hoc'), ('WY', 'Weekly'), ('FN', 'Fortnightly'), ('MO', 'Monthly')], default='FN', max_length=2, verbose_name='Payment Frequency'),
        ),
    ]
