# Generated by Django 5.0.6 on 2024-07-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Parties", "0006_alter_party_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="votes",
            field=models.IntegerField(default=0),
        ),
    ]
