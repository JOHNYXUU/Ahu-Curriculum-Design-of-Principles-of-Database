# Generated by Django 3.1 on 2020-10-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0031_remove_ware_wmeasureunit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ware',
            old_name='wphoto',
            new_name='wdetailphoto',
        ),
        migrations.AddField(
            model_name='ware',
            name='wlistphoto',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]