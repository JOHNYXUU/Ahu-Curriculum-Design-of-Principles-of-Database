# Generated by Django 3.0.3 on 2020-09-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_ware_whouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='hcategory',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='hpurpose',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]