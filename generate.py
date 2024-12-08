from django.contrib.auth.models import User
from trading_env.models import Asset, AssetHistory, Portfolio
from trading_env.models.choices import AssetTypeChoices
from trading_env.utils.trade import TransactionHandler
from trading_env.utils.tickers import TICKERS
from yahooquery import Ticker


def populate_assets():
    # Create asset objects according to the ticker file
    existing_tickers = Asset.objects.values_list("ticker", flat=True)
    if len(existing_tickers) > 0:
        print(f"{list(existing_tickers)} are already in the database.")
    
    print(f"Creating new asset objects...")
    instances = [
        Asset(ticker=ticker, name=name, asset_type=asset_type)
        for asset_type in TICKERS
        for ticker, name in TICKERS[asset_type]
        if ticker not in existing_tickers
    ]
    Asset.objects.bulk_create(instances)
    return True


def populate_historical_data(tickers: list, interval: str="1d", period: str="1y"):
    # Save historical data for relevant tickers
    tickers = Ticker(tickers)
    df = tickers.history(interval=interval, period=period).reset_index()
    instances = [
        AssetHistory(
            asset=Asset.objects.get(ticker=row.symbol),
            price=row.close,
            volume=row.volume,
            timestamp=row.date
        )
        for row in df.itertuples()
    ]
    AssetHistory.objects.bulk_create(instances)
    return True


def generate_initial_user():
    user = User.objects.create_user(username="trader1", password="trader1")
    portfolio = Portfolio.objects.create(user=user)
    return True
