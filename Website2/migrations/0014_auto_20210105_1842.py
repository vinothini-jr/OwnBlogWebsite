# Generated by Django 3.0.3 on 2021-01-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website2', '0013_remove_postpage_seo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
