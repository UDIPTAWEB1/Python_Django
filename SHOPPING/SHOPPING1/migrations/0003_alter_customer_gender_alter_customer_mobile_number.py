# Generated by Django 4.2.1 on 2023-05-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_customer_options_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=12),
        ),
    ]
