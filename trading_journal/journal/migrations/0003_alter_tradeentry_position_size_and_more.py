# Generated by Django 5.1.2 on 2024-10-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_alter_tradeentry_country_alter_tradeentry_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeentry',
            name='position_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tradeentry',
            name='profit_loss',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=15, null=True),
        ),
    ]
