# Generated by Django 3.2.9 on 2021-11-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211107_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='wood_type',
        ),
        migrations.AddField(
            model_name='product',
            name='wood_type',
            field=models.ManyToManyField(to='products.WoodType'),
        ),
    ]
