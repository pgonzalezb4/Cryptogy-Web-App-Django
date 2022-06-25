# Generated by Django 2.2 on 2022-06-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptogyapp', '0049_auto_20220625_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='-', max_length=4294967296)),
                ('receiver', models.CharField(default='-', max_length=4294967296)),
                ('amount', models.DecimalField(decimal_places=10, default=0.0, max_digits=19)),
                ('message', models.CharField(default='-', max_length=4294967296)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=19),
        ),
    ]
