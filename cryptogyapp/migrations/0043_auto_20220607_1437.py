# Generated by Django 2.2 on 2022-06-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0042_auto_20220607_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsadssinput',
            name='clearFile',
            field=models.FileField(upload_to='files'),
        ),
    ]