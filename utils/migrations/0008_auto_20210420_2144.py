# Generated by Django 3.2 on 2021-04-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0007_auto_20200805_2322"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectchange",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="taggeditem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
