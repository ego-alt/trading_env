from rest_framework import serializers
from trading_env.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["user", "asset", "action", "quantity", "price_at_transaction", "timestamp"]

