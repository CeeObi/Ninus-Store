# Generated by Django 4.2.6 on 2023-10-28 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninusStore', '0006_remove_order_order_name_cart_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='cart_date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 0, 36, 34, 910820)),
        ),
    ]
