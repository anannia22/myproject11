# Generated by Django 5.2.3 on 2025-06-25 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_status', models.IntegerField(choices=[(1, 'ORDER_CONFIRMED'), (3, 'ORDER_DELIVERED'), (4, 'OREDR_REJECTION')], default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_carts', to='products.product')),
            ],
        ),
    ]
