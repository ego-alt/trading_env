from rest_framework import serializers
from trading_env.models import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["id", "ticker", "name", "current_price", "asset_type"]
