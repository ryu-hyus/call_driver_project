# Generated by Django 4.2.3 on 2023-07-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calldriverapp', '0003_alter_myuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
