# Generated by Django 3.1.7 on 2021-03-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_result_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_key_store', models.CharField(max_length=200)),
                ('date_time_fields', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
