# Generated by Django 4.2.6 on 2023-10-28 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninusStore', '0002_alter_order_order_date_alter_product_collection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user_cart',
        ),
        migrations.AlterField(
            model_name='usercart',
            name='cart_date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 28, 11, 25, 7, 448995)),
        ),
    ]
