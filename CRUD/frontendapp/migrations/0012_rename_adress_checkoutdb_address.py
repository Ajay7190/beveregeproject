# Generated by Django 4.1.7 on 2023-08-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0011_rename_postoffice_checkoutdb_zip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdb',
            old_name='adress',
            new_name='address',
        ),
    ]
