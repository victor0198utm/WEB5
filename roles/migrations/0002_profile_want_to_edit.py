# Generated by Django 4.0.4 on 2022-04-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='want_to_edit',
            field=models.BooleanField(default=False),
        ),
    ]
