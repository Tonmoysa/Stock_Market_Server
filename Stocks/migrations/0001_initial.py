# Generated by Django 5.1.4 on 2025-03-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, verbose_name='Trading Date')),
                ('trade_code', models.CharField(db_index=True, max_length=20, verbose_name='Trade Code')),
                ('high', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Highest Price')),
                ('low', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Lowest Price')),
                ('open', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Opening Price')),
                ('close', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Closing Price')),
                ('volume', models.BigIntegerField(verbose_name='Trade Volume')),
            ],
            options={
                'verbose_name': 'Stock Data',
                'verbose_name_plural': 'Stock Data Entries',
                'ordering': ['-date'],
                'indexes': [models.Index(fields=['trade_code'], name='Stocks_stoc_trade_c_630eaf_idx'), models.Index(fields=['date'], name='Stocks_stoc_date_959e98_idx')],
            },
        ),
    ]
