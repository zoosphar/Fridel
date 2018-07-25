# Generated by Django 2.0.3 on 2018-07-22 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutiveInfo',
            fields=[
                ('Locationlat', models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=10)),
                ('Locationlong', models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=10)),
                ('executive', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='executive_username', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('live_location', models.CharField(max_length=100)),
                ('Amount', models.IntegerField(default=None, null=True)),
                ('Duration', models.IntegerField(default=None, null=True)),
                ('Duration_pick_drop', models.IntegerField(default=None, null=True)),
                ('order_id', models.IntegerField(default=None, null=True)),
                ('customer', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='customer_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
