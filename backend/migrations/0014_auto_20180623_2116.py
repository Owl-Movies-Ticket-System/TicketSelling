# Generated by Django 2.0.5 on 2018-06-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20180623_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateField(default='2018-06-23 21:09:44', verbose_name='订单日期'),
        ),
    ]