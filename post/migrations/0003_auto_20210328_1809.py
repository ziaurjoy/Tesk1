# Generated by Django 3.1.7 on 2021-03-28 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_search_result_store'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Search_result_store',
            new_name='SearchResultStore',
        ),
    ]