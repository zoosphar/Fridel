# Generated by Django 2.0.3 on 2019-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190402_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinfo',
            name='drop_home_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='drop_landmark',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='instructions',
            field=models.TextField(blank=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='other_package_content',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='package_content',
            field=models.CharField(choices=[('Documents Or Books', 'Documents Or Books'), ('Gadgets Or Accesories', 'Gadgets Or Accesories'), ('Clothes Or Outfits', 'Clothes Or Outfits'), ('Household Items', 'Household Items'), ('Food Or Beverages', 'Food Or Beverages'), ('Other', 'Other')], default='Documents Or Books', max_length=100),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='pickup_home_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='pickup_landmark',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]