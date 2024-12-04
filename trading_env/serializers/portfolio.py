from rest_framework import serializers
from models.portfolio import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['user', 'balance']

