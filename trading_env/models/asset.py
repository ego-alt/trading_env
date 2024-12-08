from decimal import Decimal
from django.core.cache import cache
from django.db import models
from django.utils.timezone import now
from trading_env.utils.market_data import fetch_market_price 

from .choices import AssetTypeChoices


class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    asset_type = models.CharField(max_length=6, choices=AssetTypeChoices)

    def __str__(self):
        return self.ticker
   
    @property
    def current_price(self):
        cached_price = cache.get(f"{self.ticker}_price")
        if cached_price:
            return cached_price

        price = fetch_market_price(self.ticker)
        if price is None:
            raise ValueError(f"Failed to retrieve {self.ticker} price.")
        price = round(Decimal(str(price)), 2)
        cache.set(f"{self.ticker}_price", price, timeout=30)
        return price
    

class AssetHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="price_history")
    price = models.DecimalField(max_digits=10, decimal_places=2) # Closing price
    volume = models.IntegerField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.asset.ticker} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

