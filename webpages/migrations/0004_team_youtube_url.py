# Generated by Django 3.0.7 on 2021-02-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_auto_20210221_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_url',
            field=models.URLField(default='https://youtube.com'),
            preserve_default=False,
        ),
    ]