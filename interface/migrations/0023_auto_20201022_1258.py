# Generated by Django 3.1.2 on 2020-10-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0022_auto_20200709_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubmission',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('done', 'Done'), ('queued', 'Queue'), ('error', 'Error')], default='new', max_length=32),
        ),
        migrations.AlterField(
            model_name='submission',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('done', 'Done'), ('queued', 'Queue'), ('error', 'Error')], default='new', max_length=32),
        ),
    ]
