# Generated by Django 2.2.4 on 2020-05-15 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20200515_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='percent_ownership',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
