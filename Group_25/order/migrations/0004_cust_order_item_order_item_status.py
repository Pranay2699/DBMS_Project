# Generated by Django 2.1.8 on 2019-04-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_cust_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cust_order_item',
            name='order_item_status',
            field=models.CharField(choices=[('0', 'Processing'), ('1', 'Confirmed'), ('2', 'Cancelled')], default=0, max_length=50),
        ),
    ]