# Generated by Django 2.2 on 2022-06-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0043_auto_20220607_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsadssinput',
            name='message',
            field=models.CharField(max_length=4294967296),
        ),
    ]