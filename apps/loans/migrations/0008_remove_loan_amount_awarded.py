# Generated by Django 4.1.1 on 2022-10-22 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_rename_amount_awared_loan_amount_awarded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='amount_awarded',
        ),
    ]