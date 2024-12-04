from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from trading_env.utils.trade import TransactionHandler

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_view(request):
    user = request.user
    data = request.data

    ticker = data.get("ticker")
    quantity = data.get("quantity")
    if not ticker or not quantity:
        return JsonResponse({"error": "Required fields ticker and quantity are missing."}, status=400)

    try: 
        handler = TransactionHandler(user=user)
        handler.buy_asset(ticker, quantity)
        return JsonResponse({"message": f"Successfully purchased {quantity} of {ticker}."})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
