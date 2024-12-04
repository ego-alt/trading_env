from .models import Asset, Portfolio, Transaction



class TransactionHandler:
    def __init__(self, user):
        self.user = user
        self.portfolio = Portfolio.objects.get(user=user)

    def buy_asset(self, ticker: str, amount: float) -> bool:
        """Trigger the buy order for an asset."""
        asset = Asset.objects.get(ticker=ticker)
        price = asset.current_price
        
        tot_cost = amount * price
        if tot_cost > self.portfolio.balance:
            print("Not enough funds.")
            return False

        # Deduct tot_cost from portfolio balance
        # Update user holdings
        # Create transaction record
        return True

    def sell_asset(self, ticker: str, amount: float) -> bool:
        """Trigger the sell order for an asset."""
        asset = Asset.objects.get(ticker=ticker)
        price = asset.current_price

        # Add earnings to portfolio balance
        # Update user holdings
        # Create transaction record
        return True
