# Generated by Django 2.2.4 on 2020-05-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200515_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5),
        ),
    ]
