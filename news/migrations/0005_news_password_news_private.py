# Generated by Django 4.0.4 on 2022-04-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='password',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
