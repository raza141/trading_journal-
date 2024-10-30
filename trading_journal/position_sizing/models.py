from django.db import models


class PositionSizingEntry(models.Model):
    stock_symbol = models.CharField(max_length=10)
    date = models.DateField()
    volatility = models.FloatField()
    volume = models.BigIntegerField()
    risk_level = models.FloatField()
    position_size = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_symbol} - Position Size: {self.position_size}"
