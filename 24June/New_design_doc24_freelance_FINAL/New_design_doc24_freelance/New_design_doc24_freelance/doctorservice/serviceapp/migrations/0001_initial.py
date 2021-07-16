# Generated by Django 3.2.2 on 2021-05-24 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp_label', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('otherinfo', models.CharField(blank=True, max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('short_description', models.CharField(blank=True, max_length=500)),
                ('long_description', models.CharField(blank=True, max_length=1000)),
                ('slug_domain', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LocationCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('sector', models.CharField(blank=True, max_length=30, null=True)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('google_maps_link', models.CharField(blank=True, max_length=500, null=True)),
                ('slug_city', models.SlugField(max_length=30)),
                ('slug_sector', models.SlugField(max_length=30)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doctors', models.ManyToManyField(blank=True, related_name='company_doctors', to=settings.AUTH_USER_MODEL)),
                ('domain', models.ManyToManyField(blank=True, to='serviceapp.DomainService')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(blank=True, max_length=90, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('description_service', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(max_length=30)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp_label.service_type')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate1', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('rate2', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('rate3', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('rate4', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('phone', models.CharField(max_length=12)),
                ('comment', models.CharField(max_length=200)),
                ('final_rate', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('doctor', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.locationcompany')),
            ],
        ),
        migrations.AddField(
            model_name='domainservice',
            name='services',
            field=models.ManyToManyField(blank=True, to='serviceapp.Service'),
        ),
        migrations.AddField(
            model_name='domainservice',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceapp.specializationservice'),
        ),
    ]
