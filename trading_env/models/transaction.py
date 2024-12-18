from django.db import models
from django.contrib.auth.models import User

from .asset import Asset
from .order import Order


class Transaction(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    buy_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # sell_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
