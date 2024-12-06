from decimal import Decimal, ROUND_HALF_UP

from trading_env.models import Asset, Order, Portfolio, PortfolioAsset
from trading_env.models.choices import OrderStatusChoices, OrderTypeChoices


class TransactionHandler:
    def __init__(self, user):
        self.user = user
        self.portfolio = Portfolio.objects.get(user=user)

    def buy_asset(self, ticker: str, quantity: str) -> bool:
        """Trigger the buy order for an asset."""
        quantity = Decimal(quantity)
        quantity = quantity.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        asset = Asset.objects.get(ticker=ticker)
        price = asset.current_price
        
        tot_cost = quantity * price
        tot_cost = tot_cost.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if tot_cost > self.portfolio.cash_balance:
            raise ValueError("Not enough funds.")

        # Deduct tot_cost from portfolio funds
        self.portfolio.cash_balance -= tot_cost
        self.portfolio.save()

        # Update user holdings
        portfolio_asset, created = PortfolioAsset.objects.get_or_create(
            portfolio=self.portfolio,
            asset=asset,
            defaults={'quantity': 0}
        )
        portfolio_asset.quantity += quantity
        portfolio_asset.save()

        # Create transaction record
        Order.objects.create(
            user=self.user,
            asset=asset,    
            status=OrderStatusChoices.CLOSED,
            order_type=OrderTypeChoices.BUY,
            quantity=quantity,
            price_at_transaction=price
        )
        return True


    def sell_asset(self, ticker: str, quantity: str) -> bool:
        """Trigger the sell order for an asset."""
        quantity = Decimal(quantity)
        quantity = quantity.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        asset = Asset.objects.get(ticker=ticker)
        price = asset.current_price

        try:
            portfolio_asset = PortfolioAsset.objects.get(portfolio=self.portfolio, asset__ticker=ticker)
        except PortfolioAsset.DoesNotExist():
            raise ValueError("Asset not found in portfolio.")

        if portfolio_asset.quantity < quantity:
            raise ValueError("Not enough holdings.")

        # Update user holdings
        portfolio_asset.quantity -= quantity
        if portfolio_asset.quantity == 0:
            portfolio_asset.delete()
        else:
            portfolio_asset.save()

        # Add proceeds to portfolio funds
        tot_proceeds = quantity * price
        tot_proceeds = tot_proceeds.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.portfolio.cash_balance += tot_proceeds
        self.portfolio.save()

        # Create transaction record
        Order.objects.create(
            user=self.user,
            asset=asset,    
            status=OrderStatusChoices.CLOSED,
            order_type=OrderTypeChoices.SELL,
            quantity=quantity,
            price_at_transaction=price
        )
        return True
