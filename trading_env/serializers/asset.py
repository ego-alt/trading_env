from rest_framework import serializers
from models.asset import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["id", "ticker", "name", "current_price", "asset_type"]
