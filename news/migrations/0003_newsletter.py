# Generated by Django 3.2.21 on 2023-09-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_subscribed', models.BooleanField(default=True)),
            ],
        ),
    ]