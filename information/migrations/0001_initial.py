# Generated by Django 3.0.3 on 2020-09-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=20)),
                ('wcategory', models.IntegerField()),
                ('wmeasureunit', models.CharField(max_length=5)),
                ('wprice', models.IntegerField()),
                ('wstandards', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hlocation', models.CharField(max_length=50)),
                ('harea', models.IntegerField()),
                ('hisoccupied', models.BooleanField(default=False)),
                ('hpurpose', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
