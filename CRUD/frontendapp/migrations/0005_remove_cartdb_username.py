# Generated by Django 4.1.7 on 2023-08-11 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0004_remove_signupdb_quantity_remove_signupdb_tprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='username',
        ),
    ]
