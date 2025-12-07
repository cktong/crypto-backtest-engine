# 🪙 Bitcoin Backtesting System with Hyperliquid

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Hyperliquid](https://img.shields.io/badge/Hyperliquid-API-orange.svg)](https://hyperliquid.xyz)

A comprehensive Bitcoin backtesting framework with **Hyperliquid API integration**, supporting both **spot and futures** trading with 5 pre-built strategies.

## ✨ Features

- ✅ **5 Trading Strategies**: SMA Crossover, RSI Mean Reversion, MACD Momentum, Bollinger Bands, Dual Momentum
- ✅ **Real Hyperliquid Data**: Fetch live historical data from 221+ trading pairs
- ✅ **Spot & Futures Support**: Long and short positions with futures trading
- ✅ **Comprehensive Metrics**: Sharpe ratio, max drawdown, win rate, profit factor
- ✅ **24/7 Hosting Ready**: Complete deployment scripts for cloud servers
- ✅ **Interactive Notebooks**: Jupyter notebooks for hands-on learning
- ✅ **Visualization Tools**: Detailed performance charts and analysis

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/cktong/crypto-backtest-engine.git
cd trading

# Install dependencies
pip install -r requirements.txt
```

### Run Your First Backtest

**Option 1: With Real Hyperliquid Data** (Recommended)
```bash
python3 backtest_with_hyperliquid.py
```

**Option 2: Simple Demo**
```bash
python3 simple_example.py
```

**Option 3: Interactive Notebook**
```bash
jupyter notebook bitcoin_backtest_notebook.ipynb
```

## 📊 Example Results

Using real Hyperliquid data (Nov 6 - Dec 6, 2025):

| Metric | Value |
|--------|-------|
| **Bitcoin Market** | -13.71% ⬇️ (bearish period) |
| **SMA Strategy** | +0.38% ⬆️ (profitable even in down market!) |
| **Total Trades** | 12 (6 long, 6 short) |
| **Win Rate** | 41.67% |
| **Max Drawdown** | 13.38% |

**Key Insight**: Short selling capability allowed profits even when Bitcoin fell 13.71%!

## 🎯 Available Strategies

### 1. SMA Crossover
Trend-following strategy using moving average crossovers.
```python
bt.run_strategy('sma_crossover', fast_period=20, slow_period=50, allow_short=True)
```

### 2. RSI Mean Reversion
Buy oversold, sell overbought conditions.
```python
bt.run_strategy('rsi_mean_reversion', oversold=30, overbought=70, allow_short=True)
```

### 3. MACD Momentum
Momentum-based entries using MACD signals.
```python
bt.run_strategy('macd_momentum', allow_short=True)
```

### 4. Bollinger Bands
Volatility-based trading at band extremes.
```python
bt.run_strategy('bollinger_bands', allow_short=True)
```

### 5. Dual Momentum
Combined trend and momentum confirmation.
```python
bt.run_strategy('dual_momentum', allow_short=True)
```

## 💡 Basic Usage

```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

# Fetch real Bitcoin data from Hyperliquid
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# Create backtester
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt.data = df
bt.calculate_indicators()

# Run strategy with short selling enabled
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)

# Analyze results
bt.print_performance_report(metrics)
bt.plot_results()
bt.export_trades('my_trades.csv')
```

## 🌐 24/7 Hosting

Deploy your backtesting system to run continuously:

### Quick Deploy to DigitalOcean

```bash
# 1. On your server (after SSH login)
bash server_setup.sh

# 2. Access Jupyter remotely
# Open browser: http://YOUR_SERVER_IP:8888
```

**Complete guides available:**
- [HOSTING_QUICKSTART.md](HOSTING_QUICKSTART.md) - 30-minute setup guide
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - All hosting options

**Cost**: FREE for 30+ months with DigitalOcean credits ($200 free)

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute introduction
- **[HYPERLIQUID_GUIDE.md](HYPERLIQUID_GUIDE.md)** - Complete Hyperliquid API guide
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - 6 hosting options compared
- **[HOSTING_QUICKSTART.md](HOSTING_QUICKSTART.md)** - Step-by-step deployment
- **[README.md](README.md)** - Full technical documentation

## 🔧 Advanced Features

### Multi-Coin Testing
```python
for coin in ["BTC", "ETH", "SOL", "HYPE"]:
    df = fetcher.fetch_candles(coin=coin, interval="1h")
    # ... run backtest
```

### Parameter Optimization
```python
for fast in [10, 20, 30]:
    for slow in [50, 100, 200]:
        metrics = bt.run_strategy('sma_crossover', fast, slow)
        print(f"SMA({fast}/{slow}): {metrics['total_return']:.2f}%")
```

### Strategy Comparison
```python
strategies = ['sma_crossover', 'rsi_mean_reversion', 'macd_momentum']
for strategy in strategies:
    metrics = bt.run_strategy(strategy, allow_short=True)
    # ... compare results
```

## 📦 What's Included

### Core System
- `bitcoin_backtest.py` - Main backtesting engine (36KB)
- `hyperliquid_data_fetcher.py` - Hyperliquid API client (11KB)
- `backtest_with_hyperliquid.py` - Complete integration (9KB)
- `simple_example.py` - Quick start demo (2KB)

### Interactive Learning
- `bitcoin_backtest_notebook.ipynb` - Jupyter notebook (23KB)

### Deployment Tools
- `setup_github.sh` - Automated GitHub setup (6KB)
- `server_setup.sh` - Server deployment script (7KB)

### Documentation
- Complete guides for all skill levels
- 50+ pages of documentation
- Real-world examples and tutorials

## 🎓 Supported Data

### Cryptocurrencies
- **221+ trading pairs** on Hyperliquid
- BTC, ETH, SOL, HYPE, AVAX, MATIC, OP, ARB, and more

### Timeframes
- **1m, 3m, 5m, 15m, 30m** (short-term)
- **1h, 2h, 4h, 8h, 12h** (medium-term) ⭐ Recommended
- **1d, 3d, 1w, 1M** (long-term)

### Data Limits
- Hyperliquid stores **5000 most recent candles** per interval
- 1h candles: ~7 months history
- 4h candles: ~2.3 years history
- 1d candles: ~13.7 years history

## ⚠️ Important Notes

### Backtesting Limitations
Backtests don't account for:
- Slippage (price movement during order execution)
- Liquidity issues (large orders may not fill)
- Latency delays
- Market impact

### Risk Disclaimer
**Past performance ≠ future results**

This software is for **educational purposes only**. Always:
- Start with small capital
- Use stop losses in live trading
- Monitor performance regularly
- Do your own research

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - See LICENSE file for details

## 🔗 Links

- **Repository**: https://github.com/cktong/crypto-backtest-engine
- **Hyperliquid**: https://hyperliquid.xyz
- **Documentation**: https://hyperliquid.gitbook.io/hyperliquid-docs/

## 📧 Contact

- **GitHub**: [@cktong](https://github.com/cktong)
- **Issues**: [Report bugs](https://github.com/cktong/crypto-backtest-engine/issues)

## 🎉 Getting Started

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run a backtest**: `python3 backtest_with_hyperliquid.py`
4. **Deploy to cloud** (optional): Follow [HOSTING_QUICKSTART.md](HOSTING_QUICKSTART.md)

Happy backtesting! 📈🚀

---

**⭐ If you find this useful, please star the repository!**
