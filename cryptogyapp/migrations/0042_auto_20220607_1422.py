# Generated by Django 2.2 on 2022-06-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0041_auto_20220607_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsadssinput',
            name='clearFile',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
