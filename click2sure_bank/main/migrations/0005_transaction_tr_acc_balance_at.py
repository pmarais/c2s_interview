# Generated by Django 3.2.7 on 2021-09-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_transaction_tr_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tr_acc_balance_at',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
