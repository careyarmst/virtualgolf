# Generated by Django 4.2.16 on 2024-12-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0007_alter_customer_fname_alter_customer_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_data',
            name='avg_grp_hcp',
            field=models.PositiveIntegerField(default=26),
        ),
        migrations.AlterField(
            model_name='golf_data',
            name='no_in_party',
            field=models.PositiveIntegerField(default=4),
        ),
    ]