# Generated by Django 5.0.2 on 2024-10-16 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pma', '0002_cases_created_at_cases_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='applicant_mobile_number',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='cases',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 16, 22, 21, 35, 853568)),
        ),
    ]
