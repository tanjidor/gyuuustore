# Generated by Django 5.1.5 on 2025-01-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_produk_carousel1_produk_carousel2_produk_carousel3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='tanggal',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
