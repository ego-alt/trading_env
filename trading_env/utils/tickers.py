from trading_env.models.choices import AssetTypeChoices


STOCK_TICKERS = [
    ("AAPL", "Apple"),
    ("AMZN", "Amazon"),
    ("GOOG", "Google"),
    ("MSFT", "Microsoft"),
    ("NFLX", "Netflix"),
    ("NVDA", "Nvidia"),
    ("SPOT", "Spotify"),
    ("TSLA", "Tesla"),
]

# Register different tickers under their asset types
TICKERS = {
    AssetTypeChoices.STOCK: STOCK_TICKERS
}
