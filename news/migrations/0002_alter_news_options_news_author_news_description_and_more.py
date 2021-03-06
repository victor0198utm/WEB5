# Generated by Django 4.0.4 on 2022-04-26 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_added'], 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='news',
            name='password',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='protected',
            field=models.BooleanField(default=False),
        ),
    ]
