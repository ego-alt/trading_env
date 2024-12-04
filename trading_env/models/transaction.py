from django.db import models
from django.contrib.auth.models import User

from .asset import Asset


class Transaction(models.Model):
    ACTION_CHOICES = {
        "BUY": "buy",
        "SELL": "sell",
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    action = models.CharField(max_length=4, choices=ACTION_CHOICES)
    quantity = models.PositiveIntegerField()
    price_at_transaction = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
