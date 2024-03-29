# Generated by Django 2.2.4 on 2019-09-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
