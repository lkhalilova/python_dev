# Generated by Django 4.2 on 2023-05-01 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_purchase_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
