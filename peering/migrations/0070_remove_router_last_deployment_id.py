# Generated by Django 3.1.7 on 2021-03-14 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peering", "0069_auto_20210212_1850"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="router",
            name="last_deployment_id",
        ),
    ]
