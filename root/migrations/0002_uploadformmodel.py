# Generated by Django 4.0.6 on 2022-08-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedFile', models.FileField(upload_to='')),
                ('password', models.TextField(default='0000')),
            ],
        ),
    ]
