# Generated by Django 4.2 on 2023-04-28 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_readers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='readers',
        ),
    ]
