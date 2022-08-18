# Generated by Django 3.1.2 on 2022-08-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_realtp_ordercount'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtp',
            name='optionName',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='realtp',
            name='sellTotalMoney',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='realtp',
            name='orderNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]