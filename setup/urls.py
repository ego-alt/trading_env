"""
URL configuration for trading_env project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from trading_env.views.market_data_view import market_price_view
from trading_env.views.portfolio_view import portfolio_view, portfolio_assets_view
from trading_env.views.trade_view import buy_view, sell_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("user/portfolio/", portfolio_view, name="portfolio"),
    path("user/portfolio-assets/", portfolio_assets_view, name="portfolio_assets"),
    path("user/buy/", buy_view, name="buy"),
    path("user/sell/", sell_view, name="sell"),
    path("market-price/<str:ticker>/", market_price_view, name="market_price"),
]
