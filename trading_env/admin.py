from django.contrib import admin
from trading_env.models import Asset, Transaction, Portfolio


admin.site.register(Asset)
admin.site.register(Transaction)
admin.site.register(Portfolio)


