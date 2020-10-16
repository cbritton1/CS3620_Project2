# Generated by Django 3.1.2 on 2020-10-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_time', '0009_storyloveletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorySmellyCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_name', models.CharField(max_length=200)),
                ('animal', models.CharField(max_length=200)),
                ('verb1', models.CharField(max_length=200)),
                ('noun1', models.CharField(max_length=200)),
                ('verb2', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('adjective1', models.CharField(max_length=200)),
                ('animal2', models.CharField(max_length=200)),
                ('noun2', models.CharField(max_length=200)),
                ('noun3', models.CharField(max_length=200)),
                ('relationship', models.CharField(max_length=200)),
                ('body_part', models.CharField(max_length=200)),
                ('verb3', models.CharField(max_length=200)),
                ('noun4', models.CharField(max_length=200)),
            ],
        ),
    ]
