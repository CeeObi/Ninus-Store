# Generated by Django 4.2.6 on 2023-10-28 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninusStore', '0009_rename_order_id_cart_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='order_name',
            field=models.CharField(default='admin', max_length=255),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='cart_date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 1, 45, 34, 940765)),
        ),
    ]