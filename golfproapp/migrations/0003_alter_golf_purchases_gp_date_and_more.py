# Generated by Django 4.2.16 on 2024-12-08 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0002_alter_golf_purchases_gp_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_purchases',
            name='gp_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 12, 8, 1, 16, 2, 782983, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='misc_purchases',
            name='mp_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 12, 8, 1, 16, 2, 782503, tzinfo=datetime.timezone.utc)),
        ),
    ]
