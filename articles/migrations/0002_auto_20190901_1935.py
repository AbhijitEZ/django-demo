# Generated by Django 2.2.4 on 2019-09-01 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data_added',
            new_name='date_added',
        ),
    ]