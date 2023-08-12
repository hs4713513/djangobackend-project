# Generated by Django 4.2.2 on 2023-07-18 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]