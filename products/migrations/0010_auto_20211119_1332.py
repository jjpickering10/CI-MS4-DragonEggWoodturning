# Generated by Django 3.2.9 on 2021-11-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_choices',
            field=models.IntegerField(blank=True, choices=[(5, '5% off'), (10, '10% off'), (15, '15% off'), (25, '25% off'), (50, '50% off')], null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discounted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]