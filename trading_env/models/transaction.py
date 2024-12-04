from django.db import models
from django.contrib.auth.models import User

from .asset import Asset


class ActionChoices(models.IntegerChoices):
    BUY = 1, "Buy"
    SELL = 2, "Sell"


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    action = models.CharField(max_length=4, choices=ActionChoices)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
