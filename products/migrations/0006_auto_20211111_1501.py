# Generated by Django 3.2.9 on 2021-11-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211111_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
