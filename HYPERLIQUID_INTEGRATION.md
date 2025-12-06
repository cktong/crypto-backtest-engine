# 🔗 Hyperliquid Direct Integration

## ✨ Automatic Real Data Fetching

Your backtesting system now **automatically fetches real Hyperliquid data** by default! No need to manually call the data fetcher.

---

## 🚀 Quick Start - It Just Works!

### Example 1: Simple Backtest (Uses Real Data Automatically)

```python
from bitcoin_backtest import BitcoinBacktester

# Create backtester
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)

# Load data - automatically fetches REAL Hyperliquid data!
bt.load_data(days=30)  # That's it! Real data fetched automatically

# Run strategy
bt.calculate_indicators()
metrics = bt.run_strategy('sma_crossover', allow_short=True)
bt.print_performance_report(metrics)
```

**What happens:**
1. ✅ System tries to fetch real Bitcoin data from Hyperliquid
2. ✅ If successful, uses real market data
3. ✅ If Hyperliquid is unavailable, falls back to synthetic data
4. ✅ You get a clear message about which data source is used

---

## 📊 Data Source Options

### Option 1: Real Hyperliquid Data (DEFAULT)

```python
bt = BitcoinBacktester(initial_capital=10000)

# Automatically uses real Hyperliquid data
bt.load_data(days=30, interval="1h")

# Or explicitly specify
bt.load_data(days=30, interval="1h", use_real_data=True)
```

**Output:**
```
📡 Fetching real BTC data from Hyperliquid...
✅ Fetched 721 candles for BTC
   Date range: 2025-11-06 02:00:00 to 2025-12-06 02:00:00
📈 Bitcoin Data Summary:
   First price: $103,352.00
   Last price:  $89,186.00
✅ Using real Hyperliquid data (721 candles)
```

### Option 2: Different Coins

```python
# Fetch Ethereum data
bt.load_data(days=30, interval="1h", coin="ETH")

# Fetch Solana data
bt.load_data(days=60, interval="4h", coin="SOL")

# Fetch HYPE token data
bt.load_data(days=7, interval="15m", coin="HYPE")
```

### Option 3: Different Timeframes

```python
# Short-term (15-minute candles)
bt.load_data(days=7, interval="15m")

# Medium-term (1-hour candles) - Recommended
bt.load_data(days=30, interval="1h")

# Long-term (4-hour candles)
bt.load_data(days=90, interval="4h")

# Daily candles
bt.load_data(days=365, interval="1d")
```

### Option 4: Synthetic Data (Testing Only)

```python
# Use synthetic data for testing
bt.load_data(days=365, use_real_data=False)
```

**Output:**
```
🎲 Using synthetic data (for testing)...
```

---

## 🔧 How It Works

### Automatic Fallback System

```python
# When you call:
bt.load_data(days=30)

# The system does:
# 1. Try to import hyperliquid_data_fetcher
# 2. Try to fetch real Hyperliquid data
# 3. If successful → use real data ✅
# 4. If error → show warning and use synthetic data 🎲
```

### Smart Error Handling

**Scenario 1: Success (Real Data)**
```
📡 Fetching real BTC data from Hyperliquid...
✅ Fetched 721 candles for BTC
✅ Using real Hyperliquid data (721 candles)
```

**Scenario 2: Network Issue**
```
📡 Fetching real BTC data from Hyperliquid...
⚠️  Error fetching Hyperliquid data: Connection timeout
    Using synthetic data instead...
```

**Scenario 3: Module Not Found**
```
⚠️  hyperliquid_data_fetcher not found, using synthetic data...
```

All scenarios work seamlessly - your backtest always runs!

---

## 💡 Use Cases

### Case 1: Production Strategy Testing

```python
# Test your strategy on REAL market data
bt = BitcoinBacktester(initial_capital=10000)
bt.load_data(days=30, interval="1h")  # Real data
bt.calculate_indicators()
metrics = bt.run_strategy('macd_momentum', allow_short=True)

# Results reflect actual market performance ✅
```

### Case 2: Quick Algorithm Testing

```python
# Test algorithm logic with synthetic data
bt = BitcoinBacktester(initial_capital=10000)
bt.load_data(days=365, use_real_data=False)  # Synthetic
bt.calculate_indicators()
metrics = bt.run_strategy('sma_crossover', allow_short=True)

# Fast, no API calls, good for dev testing
```

### Case 3: Multi-Coin Strategy

```python
# Test on multiple coins automatically
for coin in ["BTC", "ETH", "SOL"]:
    bt = BitcoinBacktester(initial_capital=10000)
    bt.load_data(days=30, interval="1h", coin=coin)
    bt.calculate_indicators()
    metrics = bt.run_strategy('rsi_mean_reversion')
    print(f"{coin}: {metrics['total_return']:.2f}%")
```

### Case 4: Timeframe Optimization

```python
# Find best timeframe for your strategy
for interval in ["15m", "1h", "4h", "1d"]:
    bt = BitcoinBacktester(initial_capital=10000)
    bt.load_data(days=30, interval=interval)
    bt.calculate_indicators()
    metrics = bt.run_strategy('bollinger_bands')
    print(f"{interval}: {metrics['total_return']:.2f}%")
```

---

## 📚 Complete API Reference

### `load_data()` Parameters

```python
bt.load_data(
    data=None,           # Optional: Pre-loaded DataFrame
    days=365,            # Number of days to fetch
    coin="BTC",          # Trading pair (BTC, ETH, SOL, etc.)
    interval="1d",       # Candle interval (1m, 5m, 15m, 1h, 4h, 1d, etc.)
    use_real_data=True   # True: fetch real data, False: synthetic
)
```

### Supported Intervals

| Interval | Description | Max Days Available* |
|----------|-------------|-------------------|
| `1m` | 1 minute | ~3.5 days |
| `5m` | 5 minutes | ~17 days |
| `15m` | 15 minutes | ~52 days |
| `1h` | 1 hour | **~208 days** ⭐ |
| `4h` | 4 hours | **~833 days** ⭐ |
| `1d` | 1 day | **~13.7 years** ⭐ |

*Hyperliquid stores 5000 most recent candles per interval

### Supported Coins

Over **221 trading pairs** including:
- Major: BTC, ETH, SOL, AVAX, MATIC
- DeFi: UNI, AAVE, LINK, CRV
- Layer 2: ARB, OP, MATIC
- Meme: DOGE, SHIB, PEPE
- Platform: HYPE (Hyperliquid token)
- And 200+ more...

To see all available coins:
```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
fetcher = HyperliquidDataFetcher()
coins = fetcher.get_available_coins()
print(f"Available: {len(coins)} coins")
```

---

## 🎯 Best Practices

### 1. Use Real Data for Final Testing

```python
# Development: Use synthetic for speed
bt.load_data(days=365, use_real_data=False)

# Production: Use real data for accuracy
bt.load_data(days=30, interval="1h", use_real_data=True)
```

### 2. Choose Appropriate Timeframes

```python
# Day trading strategies → 15m or 1h
bt.load_data(days=14, interval="15m")

# Swing trading strategies → 1h or 4h ⭐ Recommended
bt.load_data(days=60, interval="1h")

# Position trading strategies → 4h or 1d
bt.load_data(days=365, interval="1d")
```

### 3. Handle Data Fetch Failures Gracefully

The system already does this automatically, but you can check:

```python
bt = BitcoinBacktester(initial_capital=10000)
bt.load_data(days=30, interval="1h")

# Check data source
if len(bt.data) > 0:
    print(f"✅ Loaded {len(bt.data)} candles")
    first_price = bt.data['close'].iloc[0]
    
    # Heuristic: Real data usually has realistic prices
    if 10000 < first_price < 200000:  # Bitcoin range
        print("✅ Likely using real data")
    else:
        print("⚠️  Likely using synthetic data")
```

### 4. Cache Data for Repeated Tests

```python
# Fetch once
bt = BitcoinBacktester(initial_capital=10000)
bt.load_data(days=30, interval="1h")
data_copy = bt.data.copy()

# Reuse for multiple tests
for strategy in ['sma_crossover', 'rsi_mean_reversion', 'macd_momentum']:
    bt = BitcoinBacktester(initial_capital=10000)
    bt.data = data_copy.copy()  # Reuse data
    bt.calculate_indicators()
    metrics = bt.run_strategy(strategy)
    print(f"{strategy}: {metrics['total_return']:.2f}%")
```

---

## 🚨 Troubleshooting

### Issue: "hyperliquid_data_fetcher not found"

**Solution:** Make sure the file is in the same directory:
```bash
ls -la hyperliquid_data_fetcher.py
```

If missing, the system automatically falls back to synthetic data.

### Issue: "Failed to fetch Hyperliquid data"

**Possible causes:**
1. No internet connection
2. Hyperliquid API temporarily down
3. Rate limiting

**Solution:** System automatically uses synthetic data. Try again later or check:
```python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_candles(coin="BTC", interval="1h")
print(len(df))  # Should show number of candles
```

### Issue: "No data fetched"

**Cause:** Requesting more history than available

**Solution:** Hyperliquid only stores 5000 recent candles
```python
# Too much data requested
bt.load_data(days=300, interval="1h")  # Only ~208 days available!

# Correct request
bt.load_data(days=180, interval="1h")  # Within limits ✅
```

---

## 🎉 Summary

### What's Changed

**Before:**
```python
# Manual data fetching required
from hyperliquid_data_fetcher import HyperliquidDataFetcher
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(...)

bt = BitcoinBacktester()
bt.data = df  # Manual assignment
```

**Now:**
```python
# Automatic - just works!
bt = BitcoinBacktester()
bt.load_data(days=30)  # Real data automatically ✅
```

### Key Benefits

1. ✅ **Automatic**: Real data by default
2. ✅ **Reliable**: Falls back to synthetic if needed
3. ✅ **Flexible**: Easy to switch between real and synthetic
4. ✅ **Multi-coin**: Support for 221+ trading pairs
5. ✅ **Multi-timeframe**: From 1m to 1M intervals
6. ✅ **Production-ready**: Real market data for accurate backtests

### Quick Commands

```python
# Real Bitcoin data (1 hour candles, 30 days)
bt.load_data(days=30, interval="1h")

# Real Ethereum data (4 hour candles, 60 days)
bt.load_data(days=60, interval="4h", coin="ETH")

# Synthetic data for testing
bt.load_data(days=365, use_real_data=False)

# Daily Bitcoin data (365 days)
bt.load_data(days=365, interval="1d")
```

---

## 📖 Example Scripts

### Run the Updated Example

```bash
# New example with automatic real data
python3 simple_example_updated.py
```

This will:
1. ✅ Fetch real Hyperliquid data automatically
2. ✅ Run backtest with real market conditions
3. ✅ Compare with synthetic data
4. ✅ Show you the difference

### Run Original Example

```bash
# Original example (now uses real data by default!)
python3 bitcoin_backtest.py
```

This now automatically fetches real data instead of generating synthetic data.

---

## 🎯 Next Steps

1. **Test with real data**: `python3 simple_example_updated.py`
2. **Try different coins**: Test ETH, SOL, HYPE, etc.
3. **Optimize timeframes**: Find best interval for your strategy
4. **Deploy to server**: Use 24/7 with real data
5. **Paper trade**: Validate strategies with live data

**Your backtesting system is now connected to real market data!** 🚀
