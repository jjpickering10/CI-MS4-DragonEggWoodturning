# Generated by Django 3.2.9 on 2021-11-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='Sorry, no description currently', max_length=254),
        ),
    ]
