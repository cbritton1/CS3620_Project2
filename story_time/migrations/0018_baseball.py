# Generated by Django 3.1.2 on 2020-10-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_time', '0017_catandthefiddle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baseball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_name', models.CharField(max_length=200)),
                ('noun1', models.CharField(max_length=200)),
                ('verb1', models.CharField(max_length=200)),
                ('noun2', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('verb2', models.CharField(max_length=200)),
                ('adjective', models.CharField(max_length=200)),
                ('noun3', models.CharField(max_length=200)),
                ('noun4', models.CharField(max_length=200)),
            ],
        ),
    ]
