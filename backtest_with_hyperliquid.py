#!/usr/bin/env python3
"""
Bitcoin Backtesting with Hyperliquid Real Data
===============================================
Complete example integrating Hyperliquid API data with the backtesting system.

Author: AI Assistant
Date: 2025
"""

from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester
import pandas as pd


def backtest_with_hyperliquid_data(coin: str = "BTC",
                                   interval: str = "1h", 
                                   days_back: int = 30,
                                   strategy: str = "sma_crossover",
                                   initial_capital: float = 10000,
                                   allow_short: bool = True):
    """
    Run backtest using real Hyperliquid data.
    
    Args:
        coin: Trading pair (e.g., "BTC", "ETH", "SOL")
        interval: Candle interval
        days_back: Number of days to backtest
        strategy: Strategy name
        initial_capital: Starting capital
        allow_short: Enable short selling
    """
    print("\n" + "="*70)
    print(f"BACKTESTING {coin} WITH HYPERLIQUID DATA")
    print("="*70)
    
    # Step 1: Fetch data from Hyperliquid
    print("\n📡 STEP 1: Fetching data from Hyperliquid...")
    fetcher = HyperliquidDataFetcher()
    
    if coin == "BTC":
        df = fetcher.fetch_bitcoin_for_backtest(interval=interval, days_back=days_back)
    else:
        end_time = None
        start_time = None
        df = fetcher.fetch_candles(coin=coin, interval=interval)
    
    if df.empty:
        print("❌ Failed to fetch data. Exiting...")
        return None
    
    # Step 2: Initialize backtester with real data
    print(f"\n🔧 STEP 2: Initializing backtester...")
    bt = BitcoinBacktester(initial_capital=initial_capital, commission=0.001)
    bt.data = df.copy()
    
    # Step 3: Calculate technical indicators
    print(f"\n📊 STEP 3: Calculating technical indicators...")
    bt.calculate_indicators()
    
    # Step 4: Run strategy
    print(f"\n🚀 STEP 4: Running {strategy.upper()} strategy...")
    print(f"   Short selling: {'ENABLED' if allow_short else 'DISABLED'}")
    
    if strategy == "sma_crossover":
        metrics = bt.run_strategy('sma_crossover', 
                                 fast_period=20, 
                                 slow_period=50, 
                                 allow_short=allow_short)
    elif strategy == "rsi_mean_reversion":
        metrics = bt.run_strategy('rsi_mean_reversion', 
                                 oversold=30, 
                                 overbought=70, 
                                 allow_short=allow_short)
    elif strategy == "macd_momentum":
        metrics = bt.run_strategy('macd_momentum', 
                                 allow_short=allow_short)
    elif strategy == "bollinger_bands":
        metrics = bt.run_strategy('bollinger_bands', 
                                 allow_short=allow_short)
    elif strategy == "dual_momentum":
        metrics = bt.run_strategy('dual_momentum', 
                                 allow_short=allow_short)
    else:
        print(f"❌ Unknown strategy: {strategy}")
        return None
    
    # Step 5: Display results
    print(f"\n📈 STEP 5: Performance Results")
    bt.print_performance_report(metrics)
    
    # Step 6: Visualize
    print(f"\n📊 STEP 6: Generating visualization...")
    bt.plot_results()
    
    # Step 7: Export trades
    print(f"\n💾 STEP 7: Exporting trade history...")
    filename = f'{coin.lower()}_hyperliquid_trades.csv'
    bt.export_trades(filename)
    
    print("\n" + "="*70)
    print("✅ BACKTEST COMPLETE!")
    print("="*70)
    print(f"\n📁 Files generated:")
    print(f"   - backtest_results.png (visualization)")
    print(f"   - {filename} (trade history)")
    
    return bt, metrics


def compare_strategies_with_real_data(coin: str = "BTC",
                                     interval: str = "1h",
                                     days_back: int = 30):
    """
    Compare all strategies using real Hyperliquid data.
    
    Args:
        coin: Trading pair
        interval: Candle interval
        days_back: Number of days to backtest
    """
    print("\n" + "="*70)
    print(f"STRATEGY COMPARISON - {coin} (Real Hyperliquid Data)")
    print("="*70)
    
    # Fetch data once
    print("\n📡 Fetching data from Hyperliquid...")
    fetcher = HyperliquidDataFetcher()
    df = fetcher.fetch_bitcoin_for_backtest(interval=interval, days_back=days_back)
    
    if df.empty:
        print("❌ Failed to fetch data")
        return
    
    # Test all strategies
    strategies = [
        'sma_crossover',
        'rsi_mean_reversion',
        'macd_momentum',
        'bollinger_bands',
        'dual_momentum'
    ]
    
    results = {}
    
    for strategy in strategies:
        print(f"\n{'='*70}")
        print(f"Testing: {strategy.upper()}")
        print('='*70)
        
        bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
        bt.data = df.copy()
        bt.calculate_indicators()
        
        if strategy == 'sma_crossover':
            metrics = bt.run_strategy('sma_crossover', fast_period=20, slow_period=50, allow_short=True)
        elif strategy == 'rsi_mean_reversion':
            metrics = bt.run_strategy('rsi_mean_reversion', oversold=30, overbought=70, allow_short=True)
        elif strategy == 'macd_momentum':
            metrics = bt.run_strategy('macd_momentum', allow_short=True)
        elif strategy == 'bollinger_bands':
            metrics = bt.run_strategy('bollinger_bands', allow_short=True)
        elif strategy == 'dual_momentum':
            metrics = bt.run_strategy('dual_momentum', allow_short=True)
        
        results[strategy] = metrics
        bt.print_performance_report(metrics)
    
    # Create comparison table
    print("\n" + "="*70)
    print("FINAL COMPARISON - ALL STRATEGIES")
    print("="*70)
    
    comparison_df = pd.DataFrame({
        'Strategy': list(results.keys()),
        'Return (%)': [m['total_return'] for m in results.values()],
        'Trades': [m['total_trades'] for m in results.values()],
        'Win Rate (%)': [m['win_rate'] for m in results.values()],
        'Sharpe': [m['sharpe_ratio'] for m in results.values()],
        'Max DD (%)': [m['max_drawdown'] for m in results.values()]
    })
    
    comparison_df = comparison_df.sort_values('Return (%)', ascending=False)
    
    print("\n")
    print(comparison_df.to_string(index=False))
    
    print("\n" + "="*70)
    
    # Find best strategy
    best_strategy = comparison_df.iloc[0]['Strategy']
    best_return = comparison_df.iloc[0]['Return (%)']
    
    print(f"\n🏆 WINNER: {best_strategy.upper()}")
    print(f"   Return: {best_return:.2f}%")
    print("="*70)
    
    return results


def main():
    """Main execution function with examples."""
    
    print("\n" + "="*70)
    print("HYPERLIQUID BACKTESTING SYSTEM")
    print("="*70)
    print("\nThis script demonstrates backtesting with REAL Hyperliquid data")
    print("\n⚠️  Note: Hyperliquid only stores the most recent 5000 candles")
    print("   For 1h candles: ~208 days available")
    print("   For 4h candles: ~833 days available")
    print("   For 1d candles: ~13.7 years available")
    
    # Example 1: Single strategy backtest
    print("\n" + "="*70)
    print("EXAMPLE 1: Single Strategy Backtest")
    print("="*70)
    
    bt, metrics = backtest_with_hyperliquid_data(
        coin="BTC",
        interval="1h",
        days_back=30,
        strategy="sma_crossover",
        initial_capital=10000,
        allow_short=True
    )
    
    # Example 2: Compare all strategies
    print("\n\n" + "="*70)
    print("EXAMPLE 2: Compare All Strategies")
    print("="*70)
    
    results = compare_strategies_with_real_data(
        coin="BTC",
        interval="1h",
        days_back=30
    )
    
    # Example 3: Test different coins
    print("\n\n" + "="*70)
    print("EXAMPLE 3: Test Different Cryptocurrencies")
    print("="*70)
    
    for coin in ["ETH", "SOL"]:
        print(f"\n{'='*70}")
        print(f"Testing {coin}")
        print('='*70)
        
        try:
            bt, metrics = backtest_with_hyperliquid_data(
                coin=coin,
                interval="4h",
                days_back=60,
                strategy="macd_momentum",
                initial_capital=10000,
                allow_short=True
            )
        except Exception as e:
            print(f"❌ Error testing {coin}: {e}")
    
    print("\n" + "="*70)
    print("ALL EXAMPLES COMPLETE!")
    print("="*70)
    print("\n💡 Tips:")
    print("   - Use longer intervals (4h, 1d) for more historical data")
    print("   - Try different coins: BTC, ETH, SOL, HYPE, etc.")
    print("   - Optimize strategy parameters for each coin")
    print("   - Compare results with and without short selling")


if __name__ == "__main__":
    main()
