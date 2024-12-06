# Generated by Django 4.2.16 on 2024-12-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0009_customer_gchoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_golfer',
        ),
        migrations.AlterField(
            model_name='customer',
            name='gchoice',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1),
        ),
    ]