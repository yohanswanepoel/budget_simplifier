# Generated by Django 2.2.1 on 2019-06-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20190529_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='frequency',
            field=models.CharField(choices=[('AH', 'Add Hoc'), ('AP', 'At Pay'), ('MO', 'Monthly'), ('QY', 'Quarterly')], default='AP', max_length=2, verbose_name='Expense Frequency'),
        ),
        migrations.AlterField(
            model_name='payconfiguration',
            name='frequency',
            field=models.CharField(choices=[('AH', 'Add Hoc'), ('WY', 'Weekly'), ('FN', 'Fortnightly'), ('MO', 'Monthly')], default='FN', max_length=2, verbose_name='Payment Frequency'),
        ),
    ]
