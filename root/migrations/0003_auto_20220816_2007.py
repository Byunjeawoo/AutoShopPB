# Generated by Django 3.1.2 on 2022-08-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_uploadformmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='realtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.TextField(default='')),
                ('consumerName', models.TextField(default='')),
                ('productName', models.TextField(default='')),
                ('sellTime', models.TimeField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='uploadformmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userupload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
