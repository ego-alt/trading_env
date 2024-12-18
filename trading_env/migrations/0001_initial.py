# Generated by Django 5.1.3 on 2024-12-08 20:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('asset_type', models.CharField(choices=[(1, 'Stock'), (2, 'ETF'), (3, 'Bond'), (4, 'Crypto')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='AssetHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_history', to='trading_env.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=1, max_length=10)),
                ('order_type', models.CharField(choices=[(1, 'Buy'), (2, 'Sell')], max_length=4)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_at_transaction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_env.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_balance', models.DecimalField(decimal_places=2, default=1000.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_env.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='trading_env.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('holdings_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='trading_env.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_at_transaction', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_env.asset')),
                ('buy_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_env.order')),
            ],
        ),
    ]
