# Generated by Django 2.2.4 on 2019-08-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='tododetail',
            field=models.CharField(default='---', max_length=100, verbose_name='詳細'),
        ),
    ]