import yfinance as yf

from .tickers import ALL_TICKERS


def fetch_market_price(ticker_name: str) -> float | None:
    """Retrieve current market price from Yahoo Finance"""
    ticker = yf.Ticker(ticker_name)
    return ticker.info.get("currentPrice", None)


def fetch_all_market_prices() -> dict:
    market_prices = {}
    for ticker_name in ALL_TICKERS:
        market_prices[ticker_name] = fetch_market_price(ticker_name)
    return market_prices

