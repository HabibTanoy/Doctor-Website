# Generated by Django 3.2.2 on 2021-05-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesswork',
            name='weekend',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
