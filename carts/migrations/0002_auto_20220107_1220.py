# Generated by Django 3.2.6 on 2022-01-07 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'CartItem', 'verbose_name_plural': 'CartItems'},
        ),
    ]