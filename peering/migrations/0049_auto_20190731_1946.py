# Generated by Django 2.2.2 on 2019-07-31 17:46

import netfields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("peering", "0048_auto_20190707_1854")]

    operations = [
        migrations.AlterModelOptions(
            name="community",
            options={
                "ordering": ["value", "name"],
                "verbose_name_plural": "communities",
            },
        ),
        migrations.AddField(
            model_name="directpeeringsession",
            name="local_ip_address",
            field=netfields.fields.InetAddressField(
                blank=True, max_length=39, null=True
            ),
        ),
    ]
