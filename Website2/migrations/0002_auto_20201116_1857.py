# Generated by Django 3.0.5 on 2020-11-16 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='posti',
        ),
    ]
