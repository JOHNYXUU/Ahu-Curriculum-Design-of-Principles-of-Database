# Generated by Django 3.0.3 on 2020-09-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0010_auto_20200927_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ware',
            name='wphoto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/image'),
        ),
    ]
