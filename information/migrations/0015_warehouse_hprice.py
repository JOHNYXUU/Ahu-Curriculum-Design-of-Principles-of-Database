# Generated by Django 3.0.3 on 2020-09-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0014_warehouse_hphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='hprice',
            field=models.FloatField(default=20.0),
        ),
    ]
