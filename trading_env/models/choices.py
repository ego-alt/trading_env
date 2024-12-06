from django.db import models


class AssetTypeChoices(models.IntegerChoices):
    STOCK = 1, "Stock" 
    ETF = 2, "ETF"
    BOND = 3, "Bond"
    CRYPTO = 4, "Crypto"


class OrderStatusChoices(models.IntegerChoices):
    OPEN = 1, "Open"
    CLOSED = 2, "Closed"


class OrderTypeChoices(models.IntegerChoices):
    BUY = 1, "Buy"
    SELL = 2, "Sell"

