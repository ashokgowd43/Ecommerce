# Generated by Django 3.2.25 on 2024-06-23 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
