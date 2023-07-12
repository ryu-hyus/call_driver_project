# Generated by Django 4.2.3 on 2023-07-11 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('gear_type', models.CharField(choices=[('auto', '자동'), ('manual', '수동')], default='auto', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AddressHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('raw_address', models.CharField(default='', max_length=255)),
                ('adress_type', models.CharField(choices=[('start', '출발지'), ('end', '목적지')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OperationDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('operation_day', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperationOnOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('operation_onoff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('start_section', models.CharField(default='', max_length=255)),
                ('end_section', models.CharField(default='', max_length=255)),
                ('calculated_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('start_address', models.CharField(default='', max_length=255)),
                ('end_address', models.CharField(default='', max_length=255)),
                ('order_kind', models.CharField(choices=[('order', '주문'), ('change', '변경'), ('cancel', '취소')], default='주문', max_length=255)),
                ('order_type', models.BooleanField(default=True)),
                ('is_hide', models.BooleanField(default=True)),
                ('operation_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_operationday', to='calldriverapp.operationday')),
            ],
        ),
    ]