# Generated by Django 2.0.2 on 2018-12-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmanage', '0002_auto_20181207_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unit',
            field=models.CharField(choices=[('KG', 'kilogram'), ('T', 'Ton')], default='KG', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='201812071508341785', editable=False, max_length=18, primary_key=True, serialize=False),
        ),
    ]
