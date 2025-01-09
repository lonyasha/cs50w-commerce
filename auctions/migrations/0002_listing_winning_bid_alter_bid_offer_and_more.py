# Generated by Django 5.0.4 on 2024-05-10 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winning_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_auctions', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='offer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='start_bid',
            field=models.IntegerField(),
        ),
    ]
