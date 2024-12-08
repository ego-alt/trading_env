from yahooquery import Ticker

def fetch_market_price(ticker_name: str) -> float | None:
    """Retrieve current market price from Yahoo Finance"""
    ticker = Ticker(ticker_name).financial_data
    return ticker[ticker_name].get("currentPrice", None)


def fetch_market_prices(ticker_names: list) -> dict:
    market_prices = {}
    ticker_list = Ticker(ticker_names).financial_data
    for ticker_name, data in ticker_list.items():
        market_prices[ticker_name] = data.get("currentPrice", None)
    return market_prices

