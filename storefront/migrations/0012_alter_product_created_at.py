# Generated by Django 4.2.13 on 2024-06-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0011_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
