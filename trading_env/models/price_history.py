from django.db import models
from django.utils.timezone import now

from .asset import Asset

class PriceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="price_history")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.timestamp} - {self.asset.ticker}"
