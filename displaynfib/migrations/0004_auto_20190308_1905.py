# Generated by Django 2.1.7 on 2019-03-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displaynfib', '0003_auto_20190308_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiboutput',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fiboutput',
            name='result',
            field=models.IntegerField(),
        ),
    ]