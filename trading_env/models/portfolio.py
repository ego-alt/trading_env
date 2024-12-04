from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.contrib.auth.models import User

from .asset import Asset


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Start the user with 1000 dollars to play with
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def __str__(self):
        return f"{self.id} - {self.user}"

    @property
    def holdings_value(self):
        """Total value of asset holdings"""
        portfolio_value = Decimal("0.00")
        for holding in self.assets.all():
            portfolio_value += holding.value
        return portfolio_value
    
    @property
    def total_balance(self):
        return self.cash_balance + self.holdings_value


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="assets")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.asset.ticker

    @property
    def value(self):
        value = self.asset.current_price * self.quantity
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
