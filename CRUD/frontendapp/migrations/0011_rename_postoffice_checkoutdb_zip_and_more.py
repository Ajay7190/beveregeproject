# Generated by Django 4.1.7 on 2023-08-17 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0010_alter_checkoutdb_mobile_alter_checkoutdb_postoffice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdb',
            old_name='postoffice',
            new_name='zip',
        ),
        migrations.RemoveField(
            model_name='checkoutdb',
            name='fullname',
        ),
    ]
