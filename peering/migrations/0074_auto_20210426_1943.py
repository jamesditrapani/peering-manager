# Generated by Django 3.2 on 2021-04-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peering", "0073_auto_20210425_1303"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="directpeeringsession",
            options={
                "ordering": [
                    "service_reference",
                    "local_autonomous_system",
                    "autonomous_system",
                    "ip_address",
                ]
            },
        ),
        migrations.AlterModelOptions(
            name="internetexchangepeeringsession",
            options={
                "ordering": [
                    "service_reference",
                    "autonomous_system",
                    "ixp_connection",
                    "ip_address",
                ]
            },
        ),
        migrations.AddField(
            model_name="directpeeringsession",
            name="service_reference",
            field=models.CharField(
                blank=True,
                help_text="Optional: Internal Service Reference (will auto generate if left blank)",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="service_reference",
            field=models.CharField(
                blank=True,
                help_text="Optional: Unique Internal Service Reference (will auto generate if left blank)",
                max_length=255,
                null=True,
            ),
        ),
    ]
