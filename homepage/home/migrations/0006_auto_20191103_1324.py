# Generated by Django 2.2.6 on 2019-11-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191103_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='image',
            field=models.ImageField(max_length=255, upload_to='Media/accommodations/'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='image',
            field=models.ImageField(max_length=255, upload_to='Media/attractions/'),
        ),
    ]
