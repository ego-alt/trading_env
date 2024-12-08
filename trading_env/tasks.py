from celery import shared_task
import logging
import time

from .models import Asset, AssetPriceHistory, Portfolio, PortfolioAsset, PortfolioHistory

logger = logging.getLogger(__name__)


@shared_task
def fetch_price_and_log_all_portfolio():
    custom_cache = {}
    logger.info("Starting to fetch asset prices...")
    for ticker in PortfolioAsset.objects.values_list("asset__ticker", flat=True).distinct():
        logger.info(f"Fetching price for {ticker}...")
        asset = Asset.objects.get(ticker=ticker)
        custom_cache[ticker] = asset.current_price
        time.sleep(1)
    
    logger.info("All relevant asset prices have been fetched.")
    for portfolio in Portfolio.objects.all():
        logger.info(f"Updating holdings value for {portfolio.user.username}'s portfolio...")
        PortfolioHistory.objects.create(
            portfolio=portfolio,
            cash_balance=portfolio.cash_balance,
            holdings_value=portfolio.compute_holdings_value(custom_cache)
        )
    logger.info("Portfolio values have been updated and stored.")
    return True
