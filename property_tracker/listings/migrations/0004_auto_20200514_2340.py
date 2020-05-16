# Generated by Django 2.2.4 on 2020-05-15 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200514_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='APN',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='roof_type',
            field=models.CharField(blank=True, choices=[('1', 'Asphalt'), ('2', 'Clay/Concrete'), ('3', 'Slate'), ('4', 'Metal'), ('5', 'Wood')], max_length=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='roof_year',
            field=models.CharField(blank=True, max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('1', 'Rented'), ('2', 'Vacant'), ('3', 'For Sale'), ('4', 'Under Construction'), ('5', 'Buying'), ('6', 'In Escrow'), ('7', 'Sold')], default='2', max_length=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='year_built',
            field=models.CharField(blank=True, max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_status',
            field=models.CharField(choices=[('1', 'Current'), ('2', 'Late'), ('3', '3-Day Notice'), ('4', 'Vacant'), ('5', 'Evicting')], default='2', max_length=1),
        ),
    ]
