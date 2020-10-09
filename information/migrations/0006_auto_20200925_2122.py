# Generated by Django 3.0.3 on 2020-09-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20200925_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ware',
            name='wstandards',
        ),
        migrations.AlterField(
            model_name='ware',
            name='wcategory',
            field=models.CharField(choices=[('电器', '电器'), ('数码', '数码'), ('食品', '食物'), ('图书', '图书')], max_length=10),
        ),
    ]
