from django.db import models
from trading_env.utils.market_data import fetch_market_price 


class AssetTypeChoices(models.IntegerChoices):
    STOCK = 1, "Stock" 
    ETF = 2, "ETF"
    BOND = 3, "Bond"
    CRYPTO = 4, "Crypto"
    

class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    asset_type = models.CharField(max_length=6, choices=AssetTypeChoices)

    def __str__(self):
        return self.ticker
    
    def update_price(self):
        new_price = fetch_market_price(self.ticker)
        if new_price is not None:
            self.current_price = new_price
            self.save()
