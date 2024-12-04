from django.db import models
from django.contrib.auth.models import User

from .asset import Asset


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.user}"

    @property
    def balance(self):
        portfolio_value = 0
        for holding in self.portfolio_asset.all():
            portfolio_value += holding.value
        return portfolio_value


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="portfolio_asset")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.asset.ticker

    @property
    def value(self):
        return self.asset.current_price * self.quantity
