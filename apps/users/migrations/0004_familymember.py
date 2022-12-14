# Generated by Django 4.1.1 on 2022-10-01 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_member_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('relationship', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=255)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('renew_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.member')),
            ],
        ),
    ]
