# Generated by Django 4.2.1 on 2023-05-25 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_userauthor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAuthor',
            new_name='User',
        ),
    ]