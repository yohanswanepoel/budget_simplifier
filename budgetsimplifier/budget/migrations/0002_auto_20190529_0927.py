# Generated by Django 2.2.1 on 2019-05-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Expense')),
                ('frequency', models.CharField(choices=[('AH', 'Add Hoc'), ('QY', 'Quarterly'), ('AP', 'At Pay'), ('MO', 'Monthly')], default='AP', max_length=2, verbose_name='Expense Frequency')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Expense $')),
                ('day_of_month', models.IntegerField(verbose_name='Day of Month')),
            ],
        ),
        migrations.AlterField(
            model_name='payconfiguration',
            name='frequency',
            field=models.CharField(choices=[('AH', 'Add Hoc'), ('MO', 'Monthly'), ('WY', 'Weekly'), ('FN', 'Fortnightly')], default='FN', max_length=2, verbose_name='Payment Frequency'),
        ),
    ]
