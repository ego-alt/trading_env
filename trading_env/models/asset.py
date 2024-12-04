from django.db import models
from trading_env.utils.market_data import fetch_market_price 


ASSET_TYPE_CHOICES = {
    "STOCK": "stock",
    "ETF": "etf",
    "BOND": "bond",
    "CRYPTO": "crypto",
}

class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    current_price = models.DecimalField(default=0.00, decimal_places=2)
    asset_type = models.CharField(max_length=6, choices=ASSET_TYPE_CHOICES)

    def __str__(self):
        return self.ticker
    
    def update_price(self):
        new_price = fetch_market_price(self.ticker)
        if new_price is not None:
            self.current_price = new_price
            self.save()
