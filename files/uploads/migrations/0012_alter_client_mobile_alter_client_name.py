# Generated by Django 5.0.1 on 2024-01-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0011_alter_client_veh_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.IntegerField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
