# Generated by Django 4.2.5 on 2024-03-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0005_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.TextField(null=True),
        ),
    ]