"""
Hyperliquid Data Fetcher
=========================
Fetch historical Bitcoin (and other crypto) price data from Hyperliquid API
for use with the Bitcoin backtesting system.

Author: AI Assistant
Date: 2025
"""

import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, List
import time


class HyperliquidDataFetcher:
    """
    Fetch historical OHLCV data from Hyperliquid API.
    
    Hyperliquid provides candle data through their public info endpoint.
    Only the most recent 5000 candles are available.
    """
    
    def __init__(self):
        """Initialize the Hyperliquid data fetcher."""
        self.base_url = "https://api.hyperliquid.xyz/info"
        self.headers = {"Content-Type": "application/json"}
        
    def fetch_candles(self, 
                     coin: str = "BTC",
                     interval: str = "1h",
                     start_time: Optional[int] = None,
                     end_time: Optional[int] = None,
                     max_candles: int = 5000) -> pd.DataFrame:
        """
        Fetch candle data from Hyperliquid.
        
        Args:
            coin: Trading pair (e.g., "BTC", "ETH", "SOL")
            interval: Candle interval - "1m", "3m", "5m", "15m", "30m", "1h", 
                     "2h", "4h", "8h", "12h", "1d", "3d", "1w", "1M"
            start_time: Start time in epoch milliseconds (optional)
            end_time: End time in epoch milliseconds (optional)
            max_candles: Maximum number of candles to fetch (default 5000)
            
        Returns:
            DataFrame with columns: timestamp, open, high, low, close, volume
        """
        # If no end_time specified, use current time
        if end_time is None:
            end_time = int(datetime.now().timestamp() * 1000)
        
        # If no start_time specified, calculate based on interval and max_candles
        if start_time is None:
            start_time = self._calculate_start_time(end_time, interval, max_candles)
        
        # Request body
        payload = {
            "type": "candleSnapshot",
            "req": {
                "coin": coin,
                "interval": interval,
                "startTime": start_time,
                "endTime": end_time
            }
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=self.headers)
            response.raise_for_status()
            
            candles_data = response.json()
            
            if not candles_data:
                print(f"⚠️  No data returned for {coin} with interval {interval}")
                return pd.DataFrame()
            
            # Parse candle data
            candles = []
            for candle in candles_data:
                candles.append({
                    'timestamp': pd.to_datetime(candle['t'], unit='ms'),
                    'open': float(candle['o']),
                    'high': float(candle['h']),
                    'low': float(candle['l']),
                    'close': float(candle['c']),
                    'volume': float(candle['v'])
                })
            
            df = pd.DataFrame(candles)
            df = df.sort_values('timestamp').reset_index(drop=True)
            
            print(f"✅ Fetched {len(df)} candles for {coin}")
            print(f"   Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
            
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data from Hyperliquid: {e}")
            return pd.DataFrame()
    
    def fetch_multiple_intervals(self,
                                coin: str = "BTC",
                                intervals: List[str] = ["1h", "4h", "1d"],
                                days_back: int = 30) -> dict:
        """
        Fetch data for multiple intervals.
        
        Args:
            coin: Trading pair
            intervals: List of intervals to fetch
            days_back: Number of days to look back
            
        Returns:
            Dictionary with interval as key and DataFrame as value
        """
        end_time = int(datetime.now().timestamp() * 1000)
        start_time = int((datetime.now() - timedelta(days=days_back)).timestamp() * 1000)
        
        results = {}
        for interval in intervals:
            print(f"\nFetching {interval} candles for {coin}...")
            df = self.fetch_candles(coin, interval, start_time, end_time)
            if not df.empty:
                results[interval] = df
            time.sleep(0.5)  # Be nice to the API
        
        return results
    
    def _calculate_start_time(self, end_time: int, interval: str, max_candles: int) -> int:
        """Calculate start time based on interval and desired number of candles."""
        # Convert interval to minutes
        interval_minutes = self._interval_to_minutes(interval)
        
        # Calculate milliseconds per candle
        ms_per_candle = interval_minutes * 60 * 1000
        
        # Calculate start time
        start_time = end_time - (max_candles * ms_per_candle)
        
        return start_time
    
    def _interval_to_minutes(self, interval: str) -> int:
        """Convert interval string to minutes."""
        interval_map = {
            "1m": 1,
            "3m": 3,
            "5m": 5,
            "15m": 15,
            "30m": 30,
            "1h": 60,
            "2h": 120,
            "4h": 240,
            "8h": 480,
            "12h": 720,
            "1d": 1440,
            "3d": 4320,
            "1w": 10080,
            "1M": 43200  # Approximate
        }
        return interval_map.get(interval, 60)
    
    def get_available_coins(self) -> List[str]:
        """
        Get list of available trading pairs from Hyperliquid.
        
        Returns:
            List of coin symbols
        """
        payload = {
            "type": "meta"
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=self.headers)
            response.raise_for_status()
            
            meta_data = response.json()
            coins = [asset['name'] for asset in meta_data['universe']]
            
            print(f"✅ Found {len(coins)} available coins on Hyperliquid")
            return coins
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching available coins: {e}")
            return []
    
    def fetch_bitcoin_for_backtest(self, 
                                   interval: str = "1h",
                                   days_back: int = 365) -> pd.DataFrame:
        """
        Fetch Bitcoin data formatted for the backtesting system.
        
        Args:
            interval: Candle interval
            days_back: Number of days to look back
            
        Returns:
            DataFrame ready for BitcoinBacktester
        """
        print(f"\n📊 Fetching Bitcoin data from Hyperliquid for backtesting...")
        print(f"   Interval: {interval}")
        print(f"   Days back: {days_back}")
        
        # Note: Hyperliquid only keeps 5000 recent candles
        # Calculate maximum days available for the interval
        interval_minutes = self._interval_to_minutes(interval)
        max_days_available = (5000 * interval_minutes) / (60 * 24)
        
        if days_back > max_days_available:
            print(f"⚠️  Warning: Requested {days_back} days but only {max_days_available:.1f} days available")
            print(f"   Hyperliquid only stores the most recent 5000 candles")
            days_back = int(max_days_available)
        
        # Fetch the data
        df = self.fetch_candles(
            coin="BTC",
            interval=interval,
            start_time=int((datetime.now() - timedelta(days=days_back)).timestamp() * 1000),
            end_time=int(datetime.now().timestamp() * 1000)
        )
        
        if df.empty:
            print("❌ No data fetched")
            return df
        
        # Add some statistics
        print(f"\n📈 Bitcoin Data Summary:")
        print(f"   First price: ${df['close'].iloc[0]:,.2f}")
        print(f"   Last price:  ${df['close'].iloc[-1]:,.2f}")
        print(f"   Price change: {((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100:.2f}%")
        print(f"   Highest:     ${df['high'].max():,.2f}")
        print(f"   Lowest:      ${df['low'].min():,.2f}")
        print(f"   Avg volume:  {df['volume'].mean():.2f} BTC")
        
        return df
    
    def resample_to_daily(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Resample intraday data to daily candles.
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            DataFrame resampled to daily frequency
        """
        if df.empty:
            return df
        
        df_resampled = df.set_index('timestamp').resample('D').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }).dropna().reset_index()
        
        print(f"✅ Resampled to {len(df_resampled)} daily candles")
        
        return df_resampled


def example_usage():
    """Example usage of the Hyperliquid data fetcher."""
    
    print("="*60)
    print("HYPERLIQUID DATA FETCHER - EXAMPLE USAGE")
    print("="*60)
    
    # Initialize fetcher
    fetcher = HyperliquidDataFetcher()
    
    # Example 1: Get available coins
    print("\n1. Fetching available trading pairs...")
    coins = fetcher.get_available_coins()
    print(f"   Sample coins: {coins[:10]}")
    
    # Example 2: Fetch Bitcoin hourly data
    print("\n2. Fetching Bitcoin 1-hour candles...")
    btc_hourly = fetcher.fetch_bitcoin_for_backtest(interval="1h", days_back=30)
    
    if not btc_hourly.empty:
        print("\nFirst 5 rows:")
        print(btc_hourly.head())
    
    # Example 3: Fetch multiple intervals
    print("\n3. Fetching Bitcoin data at multiple intervals...")
    multi_data = fetcher.fetch_multiple_intervals(
        coin="BTC",
        intervals=["1h", "4h", "1d"],
        days_back=30
    )
    
    for interval, df in multi_data.items():
        print(f"\n{interval}: {len(df)} candles")
    
    # Example 4: Fetch and resample to daily
    print("\n4. Fetching 1-hour data and resampling to daily...")
    btc_hourly = fetcher.fetch_candles(coin="BTC", interval="1h")
    if not btc_hourly.empty:
        btc_daily = fetcher.resample_to_daily(btc_hourly)
        print("\nDaily data (last 5 days):")
        print(btc_daily.tail())
    
    # Example 5: Fetch other cryptos
    print("\n5. Fetching data for other cryptocurrencies...")
    for coin in ["ETH", "SOL", "HYPE"]:
        df = fetcher.fetch_candles(coin=coin, interval="1d")
        if not df.empty:
            print(f"\n{coin}: {len(df)} daily candles")
            print(f"   Current price: ${df['close'].iloc[-1]:,.2f}")
    
    print("\n" + "="*60)
    print("Example complete!")
    print("="*60)


if __name__ == "__main__":
    example_usage()
