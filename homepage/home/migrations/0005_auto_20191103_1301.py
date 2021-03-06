# Generated by Django 2.2.6 on 2019-11-03 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191103_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, max_length=255, upload_to='attractions/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='image',
            field=models.ImageField(max_length=255, upload_to='accommodations/'),
        ),
    ]
