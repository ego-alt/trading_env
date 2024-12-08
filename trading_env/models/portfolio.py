from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from .asset import Asset


ZERO_VALUE = Decimal("0.00")

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Start the user with 1000 dollars to play with
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def __str__(self):
        return f"{self.id} - {self.user}"

    @property
    def holdings_value(self):
        """Total value of asset holdings"""
        portfolio_value = ZERO_VALUE
        for holding in self.assets.all():
            portfolio_value += holding.value
        return portfolio_value
    
    @property
    def total_balance(self):
        return self.cash_balance + self.holdings_value

    def compute_holdings_value(self, custom_cache={}):
        """
        Calculate the total value of asset holdings according to cached prices
        Used when updating all portfolios so that asset prices are only fetched once
        """
        if not custom_cache:
            return self.holdings_value

        portfolio_value = ZERO_VALUE
        for holding in self.assets.all():
            # TODO: Handle error where custom_cache does not have the relevant ticker
            portfolio_value += round(custom_cache[holding.asset.ticker] * holding.quantity, 2)
        return portfolio_value
            
    

class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="assets")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.asset.ticker

    @property
    def value(self):
        return round(self.asset.current_price * self.quantity, 2)


class PortfolioHistory(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="history")
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    holdings_value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.portfolio.id} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
