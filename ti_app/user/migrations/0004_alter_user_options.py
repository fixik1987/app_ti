# Generated by Django 4.2.1 on 2023-05-25 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_userauthor_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'User'},
        ),
    ]
