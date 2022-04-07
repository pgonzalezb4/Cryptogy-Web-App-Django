# Generated by Django 2.2 on 2022-04-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0015_auto_20220407_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='RabinInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeP', models.BigIntegerField(blank=True)),
                ('primeQ', models.BigIntegerField(blank=True)),
                ('publicKey', models.BigIntegerField(blank=True)),
                ('clearText', models.CharField(blank=True, max_length=1200)),
                ('cipherText', models.CharField(blank=True, max_length=1200)),
            ],
        ),
    ]
