# Generated by Django 5.1.2 on 2024-10-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_tradeentry_position_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeentry',
            name='macro_event',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]