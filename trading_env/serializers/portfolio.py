from rest_framework import serializers
from trading_env.models import Portfolio, PortfolioAsset


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ["user", "cash_balance", "holdings_value", "total_balance"]


class PortfolioAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioAsset
        fields = ["portfolio", "asset", "quantity", "value"]
