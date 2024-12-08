# Generated by Django 4.2.16 on 2024-12-08 01:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0003_alter_golf_purchases_gp_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_purchases',
            name='gp_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='misc_purchases',
            name='mp_date',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]
