from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from trading_env.models import Portfolio
from trading_env.serializers.portfolio import PortfolioSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def portfolio_view(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        return JsonResponse({"error": "Portfolio not found."}, status=404)

    serializer = PortfolioSerializer(portfolio)
    return JsonResponse(serializer.data)

