# Generated by Django 4.2.16 on 2024-12-01 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0003_misc_purchases_customer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='golf_purchases',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='golf_purchases',
            name='purchase_id',
            field=models.IntegerField(default=1),
        ),
    ]
