# Generated by Django 5.0.7 on 2024-07-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBurningProfile',
            fields=[
                ('account_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('amount_burned', models.CharField(max_length=255)),
                ('balance_due', models.CharField(max_length=255)),
                ('balance_paid', models.CharField(max_length=255)),
                ('last_withdrawal', models.CharField(max_length=255)),
                ('last_burn', models.CharField(max_length=255)),
            ],
        ),
    ]
