# Generated by Django 4.1.1 on 2022-10-01 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_employment_date_employed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employment',
            old_name='postion',
            new_name='position',
        ),
    ]
