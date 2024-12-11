# Generated by Django 4.2.16 on 2024-12-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfproapp', '0002_alter_golf_data_holes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_data',
            name='holes',
            field=models.CharField(choices=[('9', '9 Holes'), ('18', '18 Holes')], default=('18', '18 Holes'), max_length=2),
        ),
    ]
