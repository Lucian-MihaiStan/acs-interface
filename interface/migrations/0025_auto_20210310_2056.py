# Generated by Django 3.1.2 on 2021-03-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0024_auto_20210124_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='assignment_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalassignment',
            name='assignment_on',
            field=models.BooleanField(default=False),
        ),
    ]