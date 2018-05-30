# Generated by Django 2.0.5 on 2018-05-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20180530_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema_movie',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='影票价格'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateField(default='2018-05-30 14:02:05', verbose_name='订单日期'),
        ),
    ]
