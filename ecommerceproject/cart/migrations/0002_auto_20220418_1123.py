# Generated by Django 3.2.12 on 2022-04-18 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Cart_Id',
            new_name='cart_id',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cart_item',
        ),
    ]
