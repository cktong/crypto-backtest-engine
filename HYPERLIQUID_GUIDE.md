# 🚀 Hyperliquid Integration Guide

Complete guide for fetching real trading data from Hyperliquid API and using it with the Bitcoin backtesting system.

## 📋 Overview

Since you trade on Hyperliquid, this integration allows you to:
- ✅ Fetch real historical Bitcoin (and other crypto) data
- ✅ Test strategies on actual market conditions
- ✅ Use your exact trading environment data
- ✅ Backtest before deploying strategies on Hyperliquid

## 🔧 Quick Start

### Option 1: Simple Backtest with Real Data

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

# Fetch real Bitcoin data from Hyperliquid
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# Run backtest
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt.data = df
bt.calculate_indicators()

# Test strategy with short selling
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)

bt.print_performance_report(metrics)
bt.plot_results()
```

### Option 2: Comprehensive Comparison

```bash
python3 backtest_with_hyperliquid.py
```

This script will:
1. Fetch real data from Hyperliquid
2. Test all 5 strategies
3. Compare performance
4. Generate visualizations
5. Export trade history

## 📊 Available Data

### Supported Cryptocurrencies

Hyperliquid supports **221 trading pairs**, including:
- **BTC** (Bitcoin)
- **ETH** (Ethereum)
- **SOL** (Solana)
- **HYPE** (Hyperliquid token)
- **AVAX**, **MATIC**, **OP**, **ARB**, and many more

To see all available coins:
```python
fetcher = HyperliquidDataFetcher()
coins = fetcher.get_available_coins()
print(coins)
```

### Supported Timeframes

Hyperliquid provides candle data at these intervals:
- **1m** (1 minute)
- **3m** (3 minutes)
- **5m** (5 minutes)
- **15m** (15 minutes)
- **30m** (30 minutes)
- **1h** (1 hour) ⭐ Recommended for backtesting
- **2h** (2 hours)
- **4h** (4 hours)
- **8h** (8 hours)
- **12h** (12 hours)
- **1d** (1 day)
- **3d** (3 days)
- **1w** (1 week)
- **1M** (1 month)

### ⚠️ Important Limitation

**Hyperliquid only stores the most recent 5000 candles** per interval.

This means:
- **1m candles**: ~3.5 days of data
- **1h candles**: ~208 days of data (7 months)
- **4h candles**: ~833 days of data (2.3 years)
- **1d candles**: ~13.7 years of data

💡 **Tip**: Use 1h or 4h intervals for good balance between detail and history.

## 🎯 Usage Examples

### Example 1: Backtest Bitcoin with Different Intervals

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

fetcher = HyperliquidDataFetcher()

# Test with 1-hour candles (more detail, shorter history)
df_1h = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=60)

# Test with 4-hour candles (less detail, longer history)
df_4h = fetcher.fetch_bitcoin_for_backtest(interval='4h', days_back=180)

# Test with daily candles (long-term view)
df_1d = fetcher.fetch_bitcoin_for_backtest(interval='1d', days_back=365)
```

### Example 2: Test Multiple Cryptocurrencies

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

fetcher = HyperliquidDataFetcher()

# Test different coins
for coin in ["BTC", "ETH", "SOL", "HYPE"]:
    print(f"\nTesting {coin}...")
    
    # Fetch data
    df = fetcher.fetch_candles(coin=coin, interval="1h")
    
    # Run backtest
    bt = BitcoinBacktester(initial_capital=10000)
    bt.data = df
    bt.calculate_indicators()
    
    metrics = bt.run_strategy('macd_momentum', allow_short=True)
    
    print(f"{coin} Return: {metrics['total_return']:.2f}%")
```

### Example 3: Compare Long-Only vs Long+Short

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# Test without short selling
bt1 = BitcoinBacktester(initial_capital=10000)
bt1.data = df.copy()
bt1.calculate_indicators()
metrics1 = bt1.run_strategy('sma_crossover', allow_short=False)

# Test with short selling
bt2 = BitcoinBacktester(initial_capital=10000)
bt2.data = df.copy()
bt2.calculate_indicators()
metrics2 = bt2.run_strategy('sma_crossover', allow_short=True)

print(f"\nLong-only:        {metrics1['total_return']:>7.2f}%")
print(f"Long+Short:       {metrics2['total_return']:>7.2f}%")
print(f"Improvement:      {metrics2['total_return'] - metrics1['total_return']:>7.2f}%")
```

### Example 4: Fetch Your Own Trading History

If you want to analyze your actual Hyperliquid trades:

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher

fetcher = HyperliquidDataFetcher()

# Note: This requires your wallet address
# The API endpoint for user fills is:
# {"type": "userFills", "user": "0xYourWalletAddress"}

# This is read-only and doesn't require authentication
# It only shows publicly visible trade data
```

## 🔑 API Details

### Hyperliquid Public API

- **Endpoint**: `https://api.hyperliquid.xyz/info`
- **Authentication**: None required (public data)
- **Rate Limits**: Be respectful, add delays between requests
- **Documentation**: https://hyperliquid.gitbook.io/hyperliquid-docs/

### Request Format

The data fetcher handles this automatically, but for reference:

```python
import requests

payload = {
    "type": "candleSnapshot",
    "req": {
        "coin": "BTC",
        "interval": "1h",
        "startTime": 1700000000000,  # epoch milliseconds
        "endTime": 1700100000000
    }
}

response = requests.post(
    "https://api.hyperliquid.xyz/info",
    json=payload,
    headers={"Content-Type": "application/json"}
)

candles = response.json()
```

### Response Format

Each candle contains:
- `t`: Timestamp (epoch milliseconds)
- `o`: Open price
- `h`: High price
- `l`: Low price
- `c`: Close price
- `v`: Volume
- `n`: Number of trades
- `s`: Symbol
- `i`: Interval

## 📈 Real Backtest Results

Using real Hyperliquid data from the past 30 days (Nov 6 - Dec 6, 2025):

### Market Conditions
- **Bitcoin starting price**: $103,352
- **Bitcoin ending price**: $89,186
- **Price change**: -13.71% (bearish market)
- **High**: $107,519
- **Low**: $80,255

### Strategy Performance (SMA Crossover with Shorts)
- **Return**: +0.38%
- **Trades**: 12 (6 long, 6 short)
- **Win Rate**: 41.67%
- **Max Drawdown**: 13.38%
- **Sharpe Ratio**: 0.10

**Key Insight**: Even in a bearish market (-13.71%), the strategy with short selling capability managed to stay profitable (+0.38%).

## 💡 Best Practices

### 1. Choose the Right Interval

**For day trading strategies:**
- Use 1m, 5m, or 15m intervals
- Limited history (~3-50 days)
- More trades, more detail

**For swing trading strategies:**
- Use 1h or 4h intervals ⭐
- Good balance (7 months - 2 years)
- Recommended for most backtests

**For position trading strategies:**
- Use 1d interval
- Maximum history (~13 years)
- Fewer trades, long-term view

### 2. Account for Hyperliquid Fees

Hyperliquid has competitive fees:
- **Maker fee**: ~0.02% (you add liquidity)
- **Taker fee**: ~0.05% (you take liquidity)

The backtester uses 0.1% (0.001) by default, which is conservative:

```python
# Match your actual fee tier
bt = BitcoinBacktester(
    initial_capital=10000,
    commission=0.0005  # 0.05% for takers
)
```

### 3. Test on Recent Data First

Start with recent data to match current market conditions:

```python
# Test last 30 days first
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# If strategy looks good, test longer period
df = fetcher.fetch_bitcoin_for_backtest(interval='4h', days_back=180)
```

### 4. Use Multiple Timeframes

Test your strategy on different timeframes:

```python
fetcher = HyperliquidDataFetcher()

# Get data at multiple intervals
multi_data = fetcher.fetch_multiple_intervals(
    coin="BTC",
    intervals=["1h", "4h", "1d"],
    days_back=60
)

# Test on each timeframe
for interval, df in multi_data.items():
    print(f"\nTesting on {interval} timeframe...")
    # ... run backtest
```

### 5. Validate Against Market Conditions

Compare your backtest results to buy-and-hold:

```python
# Calculate buy and hold return
buy_hold_return = ((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100

# Compare
print(f"Buy & Hold:  {buy_hold_return:>7.2f}%")
print(f"Strategy:    {metrics['total_return']:>7.2f}%")
print(f"Alpha:       {metrics['total_return'] - buy_hold_return:>7.2f}%")
```

## 🔧 Advanced Features

### Resample to Different Intervals

Convert high-frequency data to lower frequency:

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher

fetcher = HyperliquidDataFetcher()

# Fetch 1-hour data
df_1h = fetcher.fetch_candles(coin="BTC", interval="1h")

# Resample to daily
df_daily = fetcher.resample_to_daily(df_1h)

print(f"1h candles: {len(df_1h)}")
print(f"Daily candles: {len(df_daily)}")
```

### Fetch Multiple Coins

Batch fetch data for portfolio backtesting:

```python
coins = ["BTC", "ETH", "SOL", "AVAX"]
data = {}

for coin in coins:
    df = fetcher.fetch_candles(coin=coin, interval="1h")
    data[coin] = df
    print(f"{coin}: {len(df)} candles")
```

### Custom Date Ranges

Fetch specific time periods:

```python
from datetime import datetime, timedelta

# Define exact date range
start = int((datetime.now() - timedelta(days=90)).timestamp() * 1000)
end = int(datetime.now().timestamp() * 1000)

df = fetcher.fetch_candles(
    coin="BTC",
    interval="1h",
    start_time=start,
    end_time=end
)
```

## 🎓 Tutorial: Complete Workflow

Here's a complete workflow from data fetching to strategy deployment:

### Step 1: Research Phase

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher

# See what's available
fetcher = HyperliquidDataFetcher()
coins = fetcher.get_available_coins()
print(f"Available coins: {len(coins)}")
```

### Step 2: Data Collection

```python
# Fetch Bitcoin data at your preferred interval
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=60)
```

### Step 3: Strategy Testing

```python
from bitcoin_backtest import BitcoinBacktester

# Test your strategy
bt = BitcoinBacktester(initial_capital=10000, commission=0.0005)
bt.data = df
bt.calculate_indicators()

metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)
```

### Step 4: Parameter Optimization

```python
# Test different parameters
results = []

for fast in [10, 20, 30]:
    for slow in [50, 100, 200]:
        bt = BitcoinBacktester(initial_capital=10000)
        bt.data = df.copy()
        bt.calculate_indicators()
        
        metrics = bt.run_strategy('sma_crossover', 
                                 fast_period=fast, 
                                 slow_period=slow,
                                 allow_short=True)
        
        results.append({
            'fast': fast,
            'slow': slow,
            'return': metrics['total_return'],
            'sharpe': metrics['sharpe_ratio']
        })

# Find best parameters
best = max(results, key=lambda x: x['return'])
print(f"Best: SMA({best['fast']}/{best['slow']})")
print(f"Return: {best['return']:.2f}%")
```

### Step 5: Validation

```python
# Test on different time periods
for days in [30, 60, 90]:
    df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=days)
    bt = BitcoinBacktester(initial_capital=10000)
    bt.data = df
    bt.calculate_indicators()
    
    metrics = bt.run_strategy('sma_crossover', 
                             fast_period=best['fast'],
                             slow_period=best['slow'],
                             allow_short=True)
    
    print(f"{days} days: {metrics['total_return']:>7.2f}%")
```

### Step 6: Deploy (Manual)

Once you're satisfied with backtest results:
1. Log into your Hyperliquid account
2. Implement the strategy manually or with a trading bot
3. Start with small position sizes
4. Monitor performance vs backtest expectations

## 🚨 Important Warnings

### 1. Backtest vs Reality

Backtests don't account for:
- **Slippage**: Price movement during order execution
- **Liquidity**: Large orders may not fill at expected prices
- **Latency**: Delays in data and order execution
- **Market impact**: Your orders may move the market

### 2. Overfitting

Don't optimize parameters too much on the same data:
- Test on multiple time periods
- Use walk-forward analysis
- Reserve some data for validation

### 3. Market Conditions Change

A strategy that works in:
- Bullish markets may fail in bearish markets
- High volatility may fail in low volatility
- Trending markets may fail in ranging markets

Test across different market conditions!

### 4. Past Performance ≠ Future Results

Classic disclaimer: **Past performance does not guarantee future results.**

Always:
- Start with small capital
- Use stop losses
- Monitor regularly
- Be prepared to adjust or stop

## 📚 Additional Resources

### Hyperliquid Documentation
- **API Docs**: https://hyperliquid.gitbook.io/hyperliquid-docs/
- **Trading Docs**: https://hyperliquid.gitbook.io/hyperliquid-docs/trading
- **Websocket API**: For real-time data streaming

### Trading Strategy Resources
- Technical Analysis Libraries: TA-Lib, pandas-ta
- Backtesting Frameworks: Backtrader, Zipline
- Risk Management: Position sizing, Kelly criterion

### Community
- Hyperliquid Discord
- Trading strategy forums
- Algorithmic trading communities

## 🎉 Conclusion

You now have a complete system to:
1. ✅ Fetch real data from Hyperliquid API
2. ✅ Backtest strategies with spot and futures
3. ✅ Analyze performance metrics
4. ✅ Optimize parameters
5. ✅ Validate across different timeframes

**Next steps:**
- Run `python3 backtest_with_hyperliquid.py` for examples
- Test your own strategy ideas
- Optimize for your risk tolerance
- Paper trade before going live

Happy backtesting! 📈🚀
