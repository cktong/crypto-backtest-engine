#!/usr/bin/env python3
"""
Simple Bitcoin Backtesting Example - With Real Hyperliquid Data
================================================================
Demonstrates automatic real data fetching from Hyperliquid API.
"""

from bitcoin_backtest import BitcoinBacktester

print("="*60)
print("Bitcoin Backtesting with REAL Hyperliquid Data")
print("="*60)
print()

# Example 1: Automatic Real Data (DEFAULT)
print("📊 Example 1: Using Real Hyperliquid Data (Automatic)")
print("-" * 60)

bt = BitcoinBacktester(initial_capital=10000, commission=0.001)

# This automatically fetches REAL data from Hyperliquid
# If Hyperliquid is unavailable, it falls back to synthetic data
bt.load_data(days=30, interval="1h", use_real_data=True)

bt.calculate_indicators()

print("\n🚀 Running SMA Crossover strategy...")
metrics = bt.run_strategy('sma_crossover', 
                         fast_period=20, 
                         slow_period=50, 
                         allow_short=True)

bt.print_performance_report(metrics)

# Visualize and export
print("📊 Generating visualization...")
bt.plot_results()
bt.export_trades('real_data_trades.csv')

print()
print("="*60)
print()

# Example 2: Synthetic Data (for testing/comparison)
print("📊 Example 2: Using Synthetic Data (Testing Only)")
print("-" * 60)

bt2 = BitcoinBacktester(initial_capital=10000, commission=0.001)

# Explicitly use synthetic data
bt2.load_data(days=365, use_real_data=False)

bt2.calculate_indicators()

print("\n🚀 Running same strategy on synthetic data...")
metrics2 = bt2.run_strategy('sma_crossover', 
                           fast_period=20, 
                           slow_period=50, 
                           allow_short=True)

bt2.print_performance_report(metrics2)

print()
print("="*60)
print("📊 Comparison: Real vs Synthetic Data")
print("="*60)
print(f"Real Data Return:      {metrics['total_return']:>7.2f}%")
print(f"Synthetic Data Return: {metrics2['total_return']:>7.2f}%")
print()
print("💡 Real data reflects actual market conditions!")
print("   Use real data for production strategies.")
print()
print("✅ Examples complete!")
print("="*60)
