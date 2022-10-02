# Generated by Django 4.1.1 on 2022-10-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('maximum_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('repayment_days', models.IntegerField()),
                ('number_of_guarators', models.IntegerField()),
                ('minimum_savings', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
