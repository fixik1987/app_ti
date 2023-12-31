# Generated by Django 4.2.1 on 2023-05-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpn', models.CharField(max_length=100)),
                ('generic_part_number', models.CharField(max_length=100)),
                ('buy_now_url', models.URLField()),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('minimum_order_quantity', models.IntegerField()),
                ('standard_pack_quantity', models.IntegerField()),
                ('export_control_classification_number', models.CharField(max_length=50)),
                ('hts_code', models.CharField(max_length=50)),
                ('pin_count', models.IntegerField()),
                ('package_type', models.CharField(max_length=50)),
                ('package_carrier', models.CharField(max_length=100)),
                ('custom_reel', models.BooleanField()),
                ('life_cycle', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=10)),
                ('price_break_quantity', models.IntegerField()),
            ],
        ),
    ]
