# Generated by Django 2.0.4 on 2018-04-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20180430_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
