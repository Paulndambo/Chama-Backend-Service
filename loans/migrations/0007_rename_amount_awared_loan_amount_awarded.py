# Generated by Django 4.1.1 on 2022-10-22 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_alter_loanapplication_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='amount_awared',
            new_name='amount_awarded',
        ),
    ]
