# 🪙 Bitcoin Backtesting System with Futures Support

A comprehensive Python backtesting framework for Bitcoin trading strategies supporting both spot (long) and futures (short) positions.

## 📋 Features

### Trading Capabilities
- ✅ **Spot Trading**: Traditional buy/sell long positions
- ✅ **Futures Trading**: Short selling and covering positions
- ✅ **Multiple Strategies**: 5 pre-built trading strategies
- ✅ **Custom Parameters**: Fully customizable strategy parameters

### Technical Indicators
- Simple Moving Averages (SMA)
- Exponential Moving Averages (EMA)
- MACD (Moving Average Convergence Divergence)
- RSI (Relative Strength Index)
- Bollinger Bands
- ATR (Average True Range)

### Performance Metrics
- Total Return & P&L
- Win Rate & Profit Factor
- Sharpe Ratio
- Maximum Drawdown
- Average Win/Loss
- Commission Costs
- Trade Statistics (long vs short)

### Visualization
- Price charts with entry/exit markers
- Portfolio value over time
- Technical indicator plots
- Individual trade P&L
- Strategy comparison charts

## 🚀 Quick Start

### Option 1: Python Script

```python
from bitcoin_backtest import BitcoinBacktester

# Initialize backtester
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)

# Load data (generates synthetic data by default)
bt.load_data(days=365)

# Calculate technical indicators
bt.calculate_indicators()

# Run a strategy
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)

# Print results
bt.print_performance_report(metrics)

# Visualize
bt.plot_results()

# Export trades
bt.export_trades('my_trades.csv')
```

### Option 2: Jupyter Notebook

Open `bitcoin_backtest_notebook.ipynb` for an interactive experience with:
- Step-by-step walkthroughs
- Multiple strategy comparisons
- Parameter optimization examples
- Detailed visualizations

### Option 3: Quick Demo

Run the built-in example:

```bash
python bitcoin_backtest.py
```

This will:
1. Load synthetic Bitcoin price data
2. Run all 5 strategies
3. Compare performance
4. Generate plots and CSV exports

## 📊 Available Strategies

### 1. SMA Crossover
Buy when fast SMA crosses above slow SMA. Short when it crosses below.

```python
bt.run_strategy('sma_crossover', 
                fast_period=20, 
                slow_period=50, 
                allow_short=True)
```

### 2. RSI Mean Reversion
Buy when RSI < oversold threshold. Short when RSI > overbought threshold.

```python
bt.run_strategy('rsi_mean_reversion', 
                oversold=30, 
                overbought=70, 
                allow_short=True)
```

### 3. MACD Momentum
Buy when MACD crosses above signal line. Short when it crosses below.

```python
bt.run_strategy('macd_momentum', allow_short=True)
```

### 4. Bollinger Bands
Buy when price touches lower band. Short when price touches upper band.

```python
bt.run_strategy('bollinger_bands', allow_short=True)
```

### 5. Dual Momentum
Combines trend (SMA) and momentum (RSI) for stronger confirmation signals.

```python
bt.run_strategy('dual_momentum', allow_short=True)
```

## 💾 Using Your Own Data

To use real Bitcoin price data:

```python
import pandas as pd

# Load your CSV data
# Required columns: timestamp, open, high, low, close, volume
your_data = pd.read_csv('bitcoin_prices.csv')

# Create backtester with your data
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt.load_data(data=your_data)
bt.calculate_indicators()

# Run strategies as normal
metrics = bt.run_strategy('sma_crossover', allow_short=True)
```

### Data Format Requirements

Your CSV should have these columns:
- `timestamp`: Date/time (any format pandas can parse)
- `open`: Opening price
- `high`: Highest price in period
- `low`: Lowest price in period
- `close`: Closing price
- `volume`: Trading volume (optional but recommended)

Example:
```
timestamp,open,high,low,close,volume
2024-01-01,42000,43000,41500,42500,1500000
2024-01-02,42500,43500,42000,43200,1800000
...
```

## 🎯 Parameter Optimization

Test different parameters to find optimal settings:

```python
# Test multiple SMA combinations
for fast in [10, 20, 30]:
    for slow in [50, 100, 200]:
        bt = BitcoinBacktester(initial_capital=10000)
        bt.data = original_data.copy()
        metrics = bt.run_strategy('sma_crossover', 
                                 fast_period=fast, 
                                 slow_period=slow)
        print(f"SMA({fast}/{slow}): Return = {metrics['total_return']:.2f}%")
```

## 📈 Understanding Results

### Performance Report Example

```
============================================================
BITCOIN BACKTESTING PERFORMANCE REPORT
============================================================

📊 CAPITAL & RETURNS
Initial Capital:        $10,000.00
Final Capital:          $12,450.00
Total P&L:              $2,450.00
Total Return:           24.50%

📈 TRADE STATISTICS
Total Trades:           45
Long Trades:            23
Short Trades:           22
Winning Trades:         28
Losing Trades:          17
Win Rate:               62.22%

💰 PROFIT METRICS
Profit Factor:          1.85
Average Trade:          $54.44
Average Win:            $145.20
Average Loss:           -$78.50

⚠️  RISK METRICS
Max Drawdown:           12.35%
Sharpe Ratio:           1.42
Total Commission:       $125.00
============================================================
```

### Key Metrics Explained

- **Total Return**: Percentage gain/loss on initial capital
- **Win Rate**: Percentage of profitable trades
- **Profit Factor**: Ratio of gross profit to gross loss (>1 is profitable)
- **Sharpe Ratio**: Risk-adjusted return (>1 is good, >2 is excellent)
- **Max Drawdown**: Largest peak-to-trough decline

## 🔧 Advanced Features

### Commission Settings

Adjust trading commissions to match your exchange:

```python
bt = BitcoinBacktester(initial_capital=10000, commission=0.002)  # 0.2%
```

### Disable Short Selling

Test long-only strategies:

```python
metrics = bt.run_strategy('sma_crossover', allow_short=False)
```

### Export Trade History

Save detailed trade logs for external analysis:

```python
bt.export_trades('trades.csv')
```

The CSV includes:
- Timestamp
- Action (buy/sell/short/cover)
- Price
- Quantity
- Position type (spot/futures)
- Commission
- Total cost

## 📦 Requirements

```bash
pip install pandas numpy matplotlib
```

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0

## 🎓 Educational Use

This backtesting system is designed for:
- Learning algorithmic trading concepts
- Testing trading hypotheses
- Understanding technical indicators
- Comparing strategy performance
- Risk management analysis

⚠️ **Disclaimer**: Past performance does not guarantee future results. This is for educational purposes only. Always do your own research before trading real money.

## 📝 Files Generated

Running the backtester creates:
- `backtest_results.png`: Comprehensive visualization
- `trades.csv`: Detailed trade history
- `best_strategy_trades.csv`: Trades from best performer

## 🤝 Extending the System

Add your own strategy:

```python
class BitcoinBacktester:
    def _strategy_custom(self, param1, param2, allow_short=True):
        """Your custom strategy logic."""
        df = self.data
        position = None
        position_size = 0
        capital = self.initial_capital
        
        for i in range(50, len(df)):
            current_price = df.iloc[i]['close']
            
            # Your buy logic
            if your_buy_condition:
                position_size = (capital * 0.95) / current_price
                self.execute_trade(i, 'buy', current_price, position_size)
                # ... position tracking
            
            # Your sell logic
            elif your_sell_condition:
                # ... exit logic
                pass
        
        # Close remaining positions
        # ...
```

Then use it:

```python
bt.run_strategy('custom', param1=value1, param2=value2)
```

## 📚 Resources

- [Technical Analysis Library](https://technical-analysis-library-in-python.readthedocs.io/)
- [Backtrader Documentation](https://www.backtrader.com/docu/)
- [Quantopian Lectures](https://www.quantopian.com/lectures)

## 🐛 Troubleshooting

### "No trades executed"
- Check that your data has enough history for the indicators
- Verify strategy parameters aren't too restrictive
- Ensure data has no gaps or missing values

### Poor performance
- Try different parameter combinations
- Consider market conditions (trending vs ranging)
- Adjust position sizing or risk management
- Test on different time periods

### Memory issues with large datasets
- Process data in chunks
- Reduce indicator lookback periods
- Use more efficient data structures

## 📞 Support

For questions or issues:
1. Check the Jupyter notebook examples
2. Review strategy documentation
3. Test with synthetic data first
4. Verify data format requirements

## 🎉 Next Steps

1. **Run the example**: `python bitcoin_backtest.py`
2. **Explore notebook**: Open `bitcoin_backtest_notebook.ipynb`
3. **Load your data**: Use real Bitcoin prices
4. **Optimize parameters**: Test different settings
5. **Create custom strategies**: Extend the framework
6. **Analyze results**: Study winning patterns

Happy backtesting! 📈🚀
