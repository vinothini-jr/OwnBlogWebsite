# Generated by Django 3.0.3 on 2020-12-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website2', '0008_postpage_seo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postpage',
            name='seo_title',
        ),
        migrations.AddField(
            model_name='postpage',
            name='seo_des',
            field=models.TextField(null=True),
        ),
    ]
