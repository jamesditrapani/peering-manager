# Generated by Django 2.1 on 2018-08-02 21:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0016_auto_20180726_1307")]

    operations = [
        migrations.AddField(
            model_name="autonomoussystem",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="community",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="community",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="configurationtemplate",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="peeringsession",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="peeringsession",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="router",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="router",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
