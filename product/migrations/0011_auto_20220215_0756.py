# Generated by Django 3.2.9 on 2022-02-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_discountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isBestSeller',
            field=models.BooleanField(default=False, verbose_name='is best seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='isNew',
            field=models.BooleanField(default=True, verbose_name='is new'),
        ),
    ]
