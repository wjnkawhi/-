# Generated by Django 2.0.2 on 2018-12-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmanage', '0003_auto_20181207_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='201812142325155089', editable=False, max_length=18, primary_key=True, serialize=False),
        ),
    ]
