# Generated by Django 3.2.2 on 2021-05-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0011_doctor_experience_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='procedures',
            field=models.ManyToManyField(blank=True, to='doctors.Procedure'),
        ),
    ]