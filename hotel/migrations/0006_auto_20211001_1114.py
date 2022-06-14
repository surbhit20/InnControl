# Generated by Django 3.2 on 2021-10-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_info_pan'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.CharField(default='null', max_length=150),
        ),
        migrations.AddField(
            model_name='info',
            name='first',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='info',
            name='last',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]