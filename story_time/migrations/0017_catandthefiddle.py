# Generated by Django 3.1.2 on 2020-10-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_time', '0016_auto_20201017_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatAndTheFiddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_name', models.CharField(max_length=200)),
                ('silly_word', models.CharField(max_length=200)),
                ('animal', models.CharField(max_length=200)),
                ('musical_instrument', models.CharField(max_length=200)),
                ('noun1', models.CharField(max_length=200)),
                ('adjective1', models.CharField(max_length=200)),
                ('noun2', models.CharField(max_length=200)),
            ],
        ),
    ]
