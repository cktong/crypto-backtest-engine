# 📓 Jupyter Notebook Guide

## 🚀 Quick Start

### Method 1: Use the Startup Script (Recommended)
```bash
cd /home/user/webapp
./start_jupyter.sh
```

### Method 2: Manual Start
```bash
cd /home/user/webapp
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --allow-root
```

### Method 3: Background Mode
```bash
cd /home/user/webapp
nohup jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --allow-root > jupyter.log 2>&1 &
```

---

## 🌐 Accessing Jupyter Notebook

### Local Access (Same Machine)
- **URL**: http://localhost:8888
- Open your browser and navigate to the URL above

### Remote Access (From Another Computer)
1. Get the public URL for port 8888 using the sandbox service
2. Or use SSH port forwarding:
   ```bash
   ssh -L 8888:localhost:8888 user@your-server
   ```
3. Then access: http://localhost:8888

---

## 📂 Available Notebooks

### Current Notebooks
- **bitcoin_backtest_notebook.ipynb** - Original Bitcoin backtesting notebook

### Create New Notebook
1. Start Jupyter (see above)
2. Navigate to http://localhost:8888
3. Click "New" → "Python 3"
4. Start coding!

---

## 💡 Quick Examples for Notebooks

### Example 1: Test Bitcoin
```python
import sys
sys.path.insert(0, '/home/user/webapp')

from core import CryptoBacktester

# Initialize for Bitcoin
bt = CryptoBacktester(asset_symbol="BTC", initial_capital=10000)

# Load data
bt.load_data(days=30, interval="1h", use_real_data=False)
bt.calculate_indicators()

# Run strategy
metrics = bt.run_strategy('sma_crossover', allow_short=True)

# Display results
bt.print_performance_report(metrics)
bt.plot_results()
```

### Example 2: Test SPDR Token
```python
from core import CryptoBacktester

# Initialize for SPDR
bt = CryptoBacktester(asset_symbol="SPDR", initial_capital=10000)

# Load data
bt.load_data(days=30, interval="1h", use_real_data=False)
bt.calculate_indicators()

# Run strategy
metrics = bt.run_strategy('sma_crossover', allow_short=True)

# Display results
bt.print_performance_report(metrics)
```

### Example 3: Compare Multiple Assets
```python
from core import CryptoBacktester
import pandas as pd

assets = ["BTC", "ETH", "SPDR", "GLAM"]
results = []

for asset in assets:
    bt = CryptoBacktester(asset_symbol=asset, initial_capital=10000)
    bt.load_data(days=30, interval="1h", use_real_data=False)
    bt.calculate_indicators()
    metrics = bt.run_strategy('sma_crossover', allow_short=True)
    
    results.append({
        'Asset': asset,
        'Return %': metrics['total_return'],
        'Win Rate %': metrics['win_rate'],
        'Sharpe Ratio': metrics['sharpe_ratio'],
        'Max Drawdown %': metrics['max_drawdown']
    })

# Display as DataFrame
df_results = pd.DataFrame(results)
print(df_results)
```

---

## 🎨 Notebook Tips

### Import Required Libraries
```python
import sys
sys.path.insert(0, '/home/user/webapp')

from core import CryptoBacktester
from data_sources import HyperliquidDataFetcher
from config import get_asset_config, list_available_assets, print_all_assets

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configure matplotlib for notebook
%matplotlib inline
```

### View All Available Assets
```python
from config import print_all_assets
print_all_assets()
```

### Fetch Real Data from Hyperliquid
```python
from data_sources import HyperliquidDataFetcher

fetcher = HyperliquidDataFetcher()

# Fetch Bitcoin data
btc_data = fetcher.fetch_for_backtest(coin="BTC", interval="1h", days=30)
print(btc_data.head())

# Fetch SPDR data
spdr_data = fetcher.fetch_for_backtest(coin="SPDR", interval="1h", days=30)
print(spdr_data.head())
```

---

## 🛑 Stopping Jupyter

### If Started in Foreground
- Press **Ctrl+C** in the terminal
- Confirm with 'y' when prompted

### If Started in Background
```bash
# Find the process
ps aux | grep jupyter

# Kill it (replace PID with actual process ID)
kill <PID>

# Or use pkill
pkill -f jupyter-notebook
```

---

## 🔧 Troubleshooting

### Port Already in Use
If port 8888 is already in use, try a different port:
```bash
jupyter notebook --ip=0.0.0.0 --port=8889 --no-browser --NotebookApp.token=''
```

### Cannot Connect Remotely
Make sure:
1. Jupyter is running with `--ip=0.0.0.0`
2. Port 8888 is accessible (check firewall)
3. You're using the correct URL

### Import Errors
If you get import errors, add the path:
```python
import sys
sys.path.insert(0, '/home/user/webapp')
```

### Kernel Dies
If the kernel keeps dying:
1. Check available memory: `free -h`
2. Reduce data size (fewer days)
3. Restart Jupyter

---

## 📦 Installing Additional Packages

### In a Notebook Cell
```python
!pip install package-name
```

### From Terminal
```bash
cd /home/user/webapp
pip install package-name
```

---

## 🎯 Useful Notebook Commands

### Magic Commands
```python
# Show available magic commands
%lsmagic

# Time execution
%time code_to_time

# Auto-reload modules
%load_ext autoreload
%autoreload 2

# Display plots inline
%matplotlib inline

# Clear all output
from IPython.display import clear_output
clear_output()
```

### Display Functions
```python
from IPython.display import display, HTML, Markdown

# Display HTML
display(HTML('<h1>Hello</h1>'))

# Display Markdown
display(Markdown('## Results'))

# Display DataFrame with styling
df.style.highlight_max(axis=0)
```

---

## 📝 Creating a New Analysis Notebook

### Template
```python
# Cell 1: Setup
import sys
sys.path.insert(0, '/home/user/webapp')

from core import CryptoBacktester
from data_sources import HyperliquidDataFetcher
from config import print_all_assets

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

print("✅ Setup complete!")

# Cell 2: View Available Assets
print_all_assets()

# Cell 3: Initialize Backtester
asset = "SPDR"  # Change this to test different assets
bt = CryptoBacktester(asset_symbol=asset, initial_capital=10000)
print(f"✅ Backtester initialized for {asset}")

# Cell 4: Load Data
bt.load_data(days=30, interval="1h", use_real_data=False)
bt.calculate_indicators()
print(f"✅ Data loaded: {len(bt.data)} candles")

# Cell 5: Run Strategy
metrics = bt.run_strategy('sma_crossover', allow_short=True)
print("✅ Strategy executed")

# Cell 6: View Results
bt.print_performance_report(metrics)

# Cell 7: Plot Results
bt.plot_results()

# Cell 8: Export Trades
bt.export_trades(f'/home/user/{asset}_trades.csv')
print(f"✅ Trades exported to {asset}_trades.csv")
```

---

## 🎉 Next Steps

1. **Start Jupyter**: `./start_jupyter.sh`
2. **Access it**: http://localhost:8888 (or use remote URL)
3. **Open notebook**: Click on `notebooks/bitcoin_backtest_notebook.ipynb`
4. **Or create new**: Click "New" → "Python 3"
5. **Start testing**: Use the examples above!

---

## 🌐 Getting Remote URL

If you're running in a sandbox/remote environment and need a public URL:

```python
# Use the GetServiceUrl tool (if available)
# This will give you a public HTTPS URL to access Jupyter from anywhere
```

The URL will look like: `https://8888-sandbox-id.e2b.dev`

---

## 📞 Need Help?

- **Jupyter Documentation**: https://jupyter-notebook.readthedocs.io/
- **Keyboard Shortcuts**: Press 'H' in notebook for help
- **Check Status**: `jupyter notebook list`
- **Server Info**: Check console output where Jupyter is running

---

**Happy Interactive Backtesting! 📈📓**
