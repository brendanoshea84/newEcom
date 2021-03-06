# Generated by Django 2.2.6 on 2021-02-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210220_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_total',
            new_name='total',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=5.99, max_digits=100),
        ),
    ]
