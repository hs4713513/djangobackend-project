# Generated by Django 4.2.2 on 2023-07-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.TextField()),
            ],
        ),
    ]
