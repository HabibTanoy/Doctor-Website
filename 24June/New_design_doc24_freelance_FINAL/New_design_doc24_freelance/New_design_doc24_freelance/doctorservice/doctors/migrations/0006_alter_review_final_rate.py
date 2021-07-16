# Generated by Django 3.2.2 on 2021-05-29 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20210528_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='final_rate',
            field=models.FloatField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]