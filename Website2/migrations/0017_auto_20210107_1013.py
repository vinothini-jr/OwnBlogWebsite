# Generated by Django 3.0.3 on 2021-01-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website2', '0016_home_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='imaging',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
    ]
