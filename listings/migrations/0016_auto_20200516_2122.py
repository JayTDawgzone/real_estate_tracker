# Generated by Django 2.2.4 on 2020-05-17 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20200516_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='monthly_pmt',
            new_name='annual_pmt',
        ),
    ]
