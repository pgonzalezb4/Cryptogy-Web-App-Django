# Generated by Django 2.2 on 2022-04-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0004_auto_20220403_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptosystem',
            name='icon',
            field=models.ImageField(default='/media/default.jpg', upload_to=''),
        ),
    ]