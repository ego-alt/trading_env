from django.db import models
from django.contrib.auth.models import User

from .asset import Asset
from .choices import OrderStatusChoices, OrderTypeChoices


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default=OrderStatusChoices.OPEN)
    order_type = models.CharField(max_length=4, choices=OrderTypeChoices)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.order_type}"
