# Generated by Django 4.0.4 on 2022-04-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='password',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]