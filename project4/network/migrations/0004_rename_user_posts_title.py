# Generated by Django 4.2.2 on 2023-07-19 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_title_posts_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='user',
            new_name='title',
        ),
    ]