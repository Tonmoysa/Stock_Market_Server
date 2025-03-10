from django.db import models

class StockData(models.Model):
    date = models.DateField(verbose_name="Trading Date", db_index=True)
    trade_code = models.CharField(max_length=20, verbose_name="Trade Code", db_index=True)
    high = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Highest Price")
    low = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Lowest Price")
    open = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Opening Price")
    close = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Closing Price")
    volume = models.BigIntegerField(verbose_name="Trade Volume")

    class Meta:
        ordering = ['-date'] 
        verbose_name = "Stock Data"
        verbose_name_plural = "Stock Data Entries"
        indexes = [
            models.Index(fields=['trade_code']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"{self.trade_code} - {self.date}"
