# Generated by Django 5.0.7 on 2024-07-19 12:53

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account_abstraction",
            "0004_rename_call_data_gas_limit_useroperation_call_gas_limit",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="safeoperation",
            name="module_address",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(db_index=True),
        ),
        migrations.AlterField(
            model_name="safeoperationconfirmation",
            name="owner",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(),
        ),
        migrations.AlterField(
            model_name="useroperation",
            name="entry_point",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(db_index=True),
        ),
        migrations.AlterField(
            model_name="useroperation",
            name="paymaster",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(
                blank=True, db_index=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="useroperation",
            name="sender",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(db_index=True),
        ),
    ]
