# Generated by Django 3.2.9 on 2021-11-09 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
