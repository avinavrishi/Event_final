# Generated by Django 3.0.2 on 2021-03-19 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='id',
        ),
        migrations.AddField(
            model_name='news',
            name='news_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
