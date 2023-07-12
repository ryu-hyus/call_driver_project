# Generated by Django 4.2.3 on 2023-07-11 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calldriverapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresshistory',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='history_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderdata',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='addresshistory',
            table='addrees history',
        ),
        migrations.AlterModelTable(
            name='myuser',
            table='myuser',
        ),
        migrations.AlterModelTable(
            name='orderdata',
            table='orderdata',
        ),
    ]