# Generated by Django 3.1.2 on 2020-12-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='balance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
