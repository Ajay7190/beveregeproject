# Generated by Django 4.1.7 on 2023-08-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0002_remove_signupdb_confrim_pswd_remove_signupdb_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='signupdb',
            name='quantity',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='signupdb',
            name='tprice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]