# Generated by Django 2.2.4 on 2020-05-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_auto_20200519_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sold_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]