# 🚀 Quick Start Guide - Bitcoin Backtesting with Hyperliquid

Get up and running in 5 minutes!

## 📦 What You Have

A complete Python backtesting system with:
- ✅ **5 trading strategies** (SMA, RSI, MACD, Bollinger Bands, Dual Momentum)
- ✅ **Spot & Futures trading** (long and short positions)
- ✅ **Real Hyperliquid data** integration
- ✅ **Performance metrics** (Sharpe ratio, max drawdown, win rate, etc.)
- ✅ **Visualization tools** (charts, trade analysis)

## ⚡ 3 Ways to Get Started

### Option 1: Simple Demo (Synthetic Data)
```bash
python3 bitcoin_backtest.py
```
- Tests all 5 strategies
- Uses synthetic Bitcoin data
- Generates plots and CSV files
- Takes ~10 seconds

### Option 2: Real Hyperliquid Data
```bash
python3 backtest_with_hyperliquid.py
```
- Fetches real BTC data from Hyperliquid
- Tests all strategies on actual market data
- Compares performance across different coins
- Takes ~30 seconds

### Option 3: Interactive Notebook
```bash
jupyter notebook bitcoin_backtest_notebook.ipynb
```
- Step-by-step walkthrough
- Modify parameters in real-time
- Experiment with strategies
- Educational and hands-on

## 🎯 Your First Backtest (5 lines of code)

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

# 1. Fetch real Bitcoin data
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# 2. Create backtester
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt.data = df

# 3. Calculate indicators
bt.calculate_indicators()

# 4. Run strategy (with short selling enabled)
metrics = bt.run_strategy('sma_crossover', fast_period=20, slow_period=50, allow_short=True)

# 5. See results
bt.print_performance_report(metrics)
bt.plot_results()
```

## 📊 Understanding Your Results

After running a backtest, you'll see:

```
============================================================
BITCOIN BACKTESTING PERFORMANCE REPORT
============================================================

📊 CAPITAL & RETURNS
Initial Capital:        $10,000.00
Final Capital:          $10,038.05    ← Your ending balance
Total P&L:              $38.05        ← Total profit/loss
Total Return:           0.38%         ← Percentage return

📈 TRADE STATISTICS
Total Trades:           12            ← Number of trades executed
Long Trades:            6             ← Buy positions
Short Trades:           6             ← Short positions
Winning Trades:         5             ← Profitable trades
Losing Trades:          7             ← Unprofitable trades
Win Rate:               41.67%        ← Percentage of wins

💰 PROFIT METRICS
Profit Factor:          1.02          ← Gross profit / Gross loss (>1 is good)
Average Trade:          $3.17         ← Average P&L per trade
Average Win:            $429.90       ← Average profit on winners
Average Loss:           $-301.63      ← Average loss on losers

⚠️  RISK METRICS
Max Drawdown:           13.38%        ← Largest peak-to-trough decline
Sharpe Ratio:           0.10          ← Risk-adjusted return (>1 is good)
Total Commission:       $235.82       ← Trading fees paid
============================================================
```

### Key Metrics to Watch:

**🎯 Total Return**: Your overall profit/loss
- Positive = Strategy made money
- Negative = Strategy lost money
- Compare to buy-and-hold

**📊 Win Rate**: Percentage of winning trades
- 50%+ is good
- But high win rate doesn't guarantee profit (size matters!)

**💪 Profit Factor**: Gross profit / Gross loss
- Above 1.0 = profitable strategy
- Above 2.0 = excellent strategy

**⚠️ Max Drawdown**: Largest loss from peak
- Lower is better
- Shows worst-case scenario
- Important for risk management

**📈 Sharpe Ratio**: Risk-adjusted returns
- Above 1.0 = good
- Above 2.0 = excellent
- Accounts for volatility

## 🎨 Interpreting the Charts

The generated plot has 4 panels:

### 1. Price & Positions
- **Green triangles (^)**: Long entry (buy)
- **Red triangles (v)**: Short entry (sell)
- **Blue X**: Exit position

### 2. Portfolio Value
- Shows your account balance over time
- Rising = making money
- Falling = losing money
- Compare to the gray dashed line (initial capital)

### 3. RSI Indicator
- **Above 70**: Overbought (potential sell signal)
- **Below 30**: Oversold (potential buy signal)
- **50 line**: Neutral

### 4. Individual Trade P&L
- **Green bars**: Profitable trades
- **Red bars**: Losing trades
- Height = profit/loss amount

## 🔧 Customizing Strategies

### Change Strategy Parameters

**SMA Crossover:**
```python
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=10,   # Faster = more trades
                         slow_period=50,   # Slower = fewer trades
                         allow_short=True)
```

**RSI Mean Reversion:**
```python
metrics = bt.run_strategy('rsi_mean_reversion', 
                         oversold=25,      # Lower = fewer buy signals
                         overbought=75,    # Higher = fewer sell signals
                         allow_short=True)
```

### Disable Short Selling

If you only want long (buy) positions:
```python
metrics = bt.run_strategy('sma_crossover', allow_short=False)
```

### Adjust Commission Rate

Match your actual Hyperliquid fees:
```python
# Maker fee (~0.02%)
bt = BitcoinBacktester(initial_capital=10000, commission=0.0002)

# Taker fee (~0.05%)
bt = BitcoinBacktester(initial_capital=10000, commission=0.0005)
```

## 📝 Files Generated

After running backtests, you'll find:

- **`backtest_results.png`**: Visualization charts
- **`trades.csv`**: Detailed trade history
- **`btc_hyperliquid_trades.csv`**: Trades from Hyperliquid data

Open these files to analyze your results!

## 🎓 Next Steps

### 1. Test Different Strategies
```bash
# Compare all 5 strategies
python3 backtest_with_hyperliquid.py
```

### 2. Try Different Coins
```python
# Test Ethereum
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_candles(coin="ETH", interval="1h")

bt = BitcoinBacktester(initial_capital=10000)
bt.data = df
bt.calculate_indicators()
metrics = bt.run_strategy('macd_momentum', allow_short=True)
```

### 3. Optimize Parameters
```python
# Test multiple parameter combinations
for fast in [10, 20, 30]:
    for slow in [50, 100]:
        metrics = bt.run_strategy('sma_crossover', 
                                 fast_period=fast, 
                                 slow_period=slow)
        print(f"SMA({fast}/{slow}): {metrics['total_return']:.2f}%")
```

### 4. Use Different Timeframes
```python
# Longer history, less detail
df = fetcher.fetch_bitcoin_for_backtest(interval='4h', days_back=180)

# Shorter history, more detail
df = fetcher.fetch_bitcoin_for_backtest(interval='15m', days_back=7)
```

## 🚨 Important Notes

### Hyperliquid Data Limitations
- Only **5000 most recent candles** available
- 1h interval = ~7 months of data
- 4h interval = ~2 years of data
- Use longer intervals for more history

### Backtesting Limitations
⚠️ Backtests don't include:
- Slippage (price movement during order)
- Liquidity issues (order not filling)
- Latency delays
- Market impact of large orders

### Risk Warning
📢 **Past performance ≠ future results**
- Always start with small capital
- Use stop losses in real trading
- Monitor performance regularly
- Be prepared to adjust strategies

## 📚 Full Documentation

- **`README.md`**: Complete system documentation
- **`HYPERLIQUID_GUIDE.md`**: Hyperliquid API integration guide
- **`bitcoin_backtest_notebook.ipynb`**: Interactive tutorial

## 💡 Pro Tips

### Tip 1: Compare to Buy-and-Hold
Always calculate if your strategy beats simply holding:
```python
buy_hold = ((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100
print(f"Strategy: {metrics['total_return']:.2f}%")
print(f"Buy & Hold: {buy_hold:.2f}%")
print(f"Alpha: {metrics['total_return'] - buy_hold:.2f}%")
```

### Tip 2: Test in Different Market Conditions
- Bull market (prices rising)
- Bear market (prices falling)
- Sideways market (range-bound)

### Tip 3: Use Multiple Strategies
Diversify by combining different strategies:
```python
# Allocate capital across strategies
capital_per_strategy = 10000 / 5

for strategy in ['sma_crossover', 'rsi_mean_reversion', 'macd_momentum']:
    bt = BitcoinBacktester(initial_capital=capital_per_strategy)
    # ... run backtest
```

### Tip 4: Keep a Trading Journal
Document your backtests:
- Strategy parameters
- Market conditions
- Performance metrics
- Lessons learned

## 🆘 Troubleshooting

### "No data fetched"
- Check internet connection
- Hyperliquid API might be temporarily down
- Try a different time range

### "No trades executed"
- Strategy conditions too strict
- Try different parameters
- Check if enough data for indicators

### "Poor performance"
- Market conditions don't suit strategy
- Try different timeframe
- Optimize parameters
- Consider trend vs ranging market

## ✅ Checklist

Before deploying any strategy:
- [ ] Backtested on at least 30 days of data
- [ ] Tested in different market conditions
- [ ] Compared to buy-and-hold benchmark
- [ ] Reviewed max drawdown (can you handle it?)
- [ ] Calculated position sizing
- [ ] Set up stop losses
- [ ] Started with small capital
- [ ] Have monitoring plan

## 🎉 You're Ready!

You now have everything to:
1. ✅ Fetch real Hyperliquid data
2. ✅ Test trading strategies
3. ✅ Analyze performance
4. ✅ Optimize parameters
5. ✅ Make data-driven trading decisions

**Start with:**
```bash
python3 backtest_with_hyperliquid.py
```

Happy trading! 📈🚀
