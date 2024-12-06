from decimal import Decimal
from django.db import models
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
        price = fetch_market_price(self.ticker)
        if price is None:
            raise ValueError(f"Failed to retrieve {self.ticker} price.")
        return Decimal(str(price))
    
