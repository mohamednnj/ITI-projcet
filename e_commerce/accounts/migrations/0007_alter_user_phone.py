# Generated by Django 5.1.1 on 2024-09-24 21:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='phone number', null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(11)]),
        ),
    ]
