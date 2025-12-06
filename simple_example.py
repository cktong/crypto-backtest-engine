#!/usr/bin/env python3
"""
Simple Bitcoin Backtesting Example
===================================
Minimal example showing how to use the Bitcoin backtesting system.
"""

from bitcoin_backtest import BitcoinBacktester

# 1. Create backtester
print("Creating backtester with $10,000 initial capital...")
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)

# 2. Load data (365 days of synthetic Bitcoin data)
print("Loading Bitcoin price data...")
bt.load_data(days=365)

# 3. Calculate technical indicators
print("Calculating technical indicators...")
bt.calculate_indicators()

# 4. Run a strategy
print("\nRunning SMA Crossover strategy (allows both long and short positions)...")
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)

# 5. Print results
bt.print_performance_report(metrics)

# 6. Visualize results
print("\nGenerating visualization...")
bt.plot_results()

# 7. Export trades
print("Exporting trade history...")
bt.export_trades('my_trades.csv')

print("\n✅ Done! Check the generated files:")
print("   - backtest_results.png (visualization)")
print("   - my_trades.csv (trade history)")

# Additional example: Test without short selling
print("\n" + "="*60)
print("Running same strategy WITHOUT short selling...")
print("="*60)

bt2 = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt2.data = bt.data.copy()
metrics2 = bt2.run_strategy('sma_crossover', 
                           fast_period=20, 
                           slow_period=50, 
                           allow_short=False)

bt2.print_performance_report(metrics2)

print("\n📊 Comparison:")
print(f"With Short Selling:    Return = {metrics['total_return']:>7.2f}%, Trades = {metrics['total_trades']}")
print(f"Without Short Selling: Return = {metrics2['total_return']:>7.2f}%, Trades = {metrics2['total_trades']}")
