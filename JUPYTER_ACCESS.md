# 🎉 Jupyter Notebook is Running!

## ✅ Server Status: **ACTIVE**

Your Jupyter Notebook server is now running and ready to use!

---

## 🌐 Access URLs

### **Public URL (Access from Anywhere)**
**https://8889-i6zuwyq7g0qs6h69g1rc3-0e616f0a.sandbox.novita.ai**

👆 **Click this link or copy/paste into your browser!**

### Local URLs (If running locally)
- http://localhost:8889/tree
- http://127.0.0.1:8889/tree

---

## 📂 Available Notebooks

Once you access the URL above, you'll see:

### Existing Notebook
- **notebooks/bitcoin_backtest_notebook.ipynb** - Bitcoin backtesting examples

### You Can Also
1. **Create new notebook**: Click "New" → "Python 3"
2. **Browse files**: Navigate through the file system
3. **Upload files**: Use the "Upload" button

---

## 💡 Quick Start in Jupyter

Once you open a notebook, try this:

### Cell 1: Setup
```python
import sys
sys.path.insert(0, '/home/user/webapp')

from core import CryptoBacktester
from config import print_all_assets

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

print("✅ Setup complete!")
```

### Cell 2: Test SPDR Token
```python
# Initialize for SPDR
bt = CryptoBacktester(asset_symbol="SPDR", initial_capital=10000)

# Load data (using synthetic data for demo)
bt.load_data(days=30, interval="1h", use_real_data=False)
bt.calculate_indicators()

# Run strategy
metrics = bt.run_strategy('sma_crossover', allow_short=True)

# Show results
bt.print_performance_report(metrics)
bt.plot_results()
```

### Cell 3: Test GLAM Token
```python
# Initialize for GLAM
bt_glam = CryptoBacktester(asset_symbol="GLAM", initial_capital=10000)
bt_glam.load_data(days=30, interval="1h", use_real_data=False)
bt_glam.calculate_indicators()
metrics_glam = bt_glam.run_strategy('sma_crossover', allow_short=True)
bt_glam.print_performance_report(metrics_glam)
```

### Cell 4: Compare Multiple Assets
```python
assets = ["BTC", "ETH", "SPDR", "GLAM"]
results = []

for asset in assets:
    bt = CryptoBacktester(asset_symbol=asset, initial_capital=10000)
    bt.load_data(days=30, interval="1h", use_real_data=False)
    bt.calculate_indicators()
    metrics = bt.run_strategy('sma_crossover', allow_short=True)
    
    results.append({
        'Asset': asset,
        'Return %': f"{metrics['total_return']:.2f}",
        'Win Rate %': f"{metrics['win_rate']:.2f}",
        'Sharpe': f"{metrics['sharpe_ratio']:.2f}"
    })

df = pd.DataFrame(results)
display(df)
```

---

## 🎯 Features Available

### In Your Notebooks
- ✅ Test any cryptocurrency (BTC, ETH, SPDR, GLAM, etc.)
- ✅ Run all 5 trading strategies
- ✅ Create custom visualizations
- ✅ Compare multiple assets side-by-side
- ✅ Export results to CSV
- ✅ Interactive analysis and exploration

### Built-in Tools
- **Core Engine**: Universal cryptocurrency backtester
- **Data Sources**: Hyperliquid API integration
- **Configuration**: 10+ pre-configured assets
- **Examples**: Ready-to-run code snippets

---

## 🛑 Stopping Jupyter

When you're done:

### From Terminal
```bash
# Find the process
ps aux | grep jupyter

# Stop it
pkill -f jupyter
```

### Or use Ctrl+C
If you started Jupyter in the foreground, press Ctrl+C twice

---

## 📝 Creating New Notebooks

1. Access the URL above
2. Navigate to the `notebooks/` folder
3. Click "New" → "Python 3"
4. Start coding!

### Suggested Notebooks to Create
- **SPDR_Analysis.ipynb** - Deep dive into SPDR token
- **GLAM_Analysis.ipynb** - Deep dive into GLAM token
- **Multi_Asset_Comparison.ipynb** - Compare all assets
- **Strategy_Optimization.ipynb** - Find best parameters
- **Real_Data_Analysis.ipynb** - Use live Hyperliquid data

---

## 🔧 Troubleshooting

### Can't Access the URL?
- Make sure you're using the **public URL** (starts with https://)
- Check that Jupyter is still running: `ps aux | grep jupyter`
- Try restarting: `pkill -f jupyter && cd /home/user/webapp && ./start_jupyter.sh`

### Import Errors?
Add this at the start of every notebook:
```python
import sys
sys.path.insert(0, '/home/user/webapp')
```

### Need Real Market Data?
Set `use_real_data=True`:
```python
bt.load_data(days=30, interval="1h", use_real_data=True)
```

---

## 📚 Documentation

For more details, check:
- **JUPYTER_GUIDE.md** - Complete Jupyter guide
- **QUICK_REFERENCE.md** - Quick commands
- **README.md** - Full documentation

---

## 🎊 You're All Set!

**Access your Jupyter Notebook here:**

# 🔗 **https://8889-i6zuwyq7g0qs6h69g1rc3-0e616f0a.sandbox.novita.ai**

**What to do:**
1. Click the URL above
2. Navigate to `notebooks/bitcoin_backtest_notebook.ipynb`
3. Or create a new notebook
4. Start testing SPDR, GLAM, and other cryptocurrencies!

**Happy Interactive Backtesting! 📈📓**

---

**Server Info:**
- Port: 8889 (auto-selected)
- Status: Running ✅
- Authentication: Disabled (for development)
- Working Directory: /home/user/webapp
