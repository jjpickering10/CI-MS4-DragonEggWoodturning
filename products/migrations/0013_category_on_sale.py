# Generated by Django 3.2.9 on 2021-11-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
