from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from trading_env.utils.market_data import fetch_market_price


@api_view(["GET", "POST"])
def market_price_view(request, ticker):
    if request.method == "GET":
        price = fetch_market_price(ticker)
        if price:
            return JsonResponse({"ticker": ticker, "price": price})
        else:
            return JsonResponse({"error": "Failed to fetch market price"}, status=500)

    elif request.method == "POST":
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
