# Generated by Django 5.0.7 on 2024-07-19 12:53

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0011_alter_token_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="address",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(
                primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="token",
            name="copy_price",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(
                blank=True,
                help_text="If provided, copy the price from the token",
                null=True,
            ),
        ),
    ]
