# Generated by Django 2.2 on 2022-06-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0040_auto_20220604_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='gammaldssinput',
            name='clearFile',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='rsadssinput',
            name='clearFile',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
