#!/bin/bash

# GitHub Repository Setup Script
# This script helps you quickly push your backtesting system to GitHub

echo "=================================="
echo "GitHub Repository Setup"
echo "=================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "This script will help you push your code to GitHub."
echo ""

# Get GitHub username
read -p "Enter your GitHub username: " GITHUB_USER

# Get repository name
read -p "Enter repository name (default: bitcoin-backtest-hyperliquid): " REPO_NAME
REPO_NAME=${REPO_NAME:-bitcoin-backtest-hyperliquid}

echo ""
echo "📝 Repository will be created at:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""

read -p "Continue? (y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "🔧 Setting up Git repository..."

# Initialize git if not already
if [ ! -d .git ]; then
    git init
    echo "✅ Git initialized"
fi

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Generated files (don't commit)
*.png
*.csv
*.log
backtest_results/
trades/

# Environment
.env
venv/
env/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

echo "✅ .gitignore created"

# Create requirements.txt
cat > requirements.txt << 'EOF'
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
requests>=2.26.0
jupyter>=1.0.0
EOF

echo "✅ requirements.txt created"

# Create README badge section
cat > README_GITHUB.md << EOF
# 🪙 Bitcoin Backtesting System with Hyperliquid

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Hyperliquid](https://img.shields.io/badge/Hyperliquid-API-orange.svg)](https://hyperliquid.xyz)

A comprehensive Bitcoin backtesting framework with Hyperliquid API integration, supporting both spot and futures trading.

## 🚀 Quick Start

\`\`\`bash
# Clone repository
git clone https://github.com/$GITHUB_USER/$REPO_NAME.git
cd $REPO_NAME

# Install dependencies
pip install -r requirements.txt

# Run backtest with real Hyperliquid data
python3 backtest_with_hyperliquid.py
\`\`\`

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md)
- [Hyperliquid Integration](HYPERLIQUID_GUIDE.md)
- [Deployment Guide](DEPLOYMENT_GUIDE.md)
- [Full Documentation](README.md)

## ✨ Features

- ✅ 5 pre-built trading strategies (SMA, RSI, MACD, Bollinger Bands, Dual Momentum)
- ✅ Real Hyperliquid API data integration
- ✅ Spot & Futures (long/short) support
- ✅ Comprehensive performance metrics
- ✅ Interactive Jupyter notebooks
- ✅ Visualization tools

## 📊 Example Results

Using real Hyperliquid data (30-day backtest):
- Bitcoin: -13.71% (market performance)
- Strategy: +0.38% (with short selling)

## 🎯 Strategies

1. **SMA Crossover** - Trend-following
2. **RSI Mean Reversion** - Oversold/overbought
3. **MACD Momentum** - Momentum-based
4. **Bollinger Bands** - Volatility trading
5. **Dual Momentum** - Combined signals

## 💡 Usage

\`\`\`python
from hyperliquid_data_fetcher import HyperliquidDataFetcher
from bitcoin_backtest import BitcoinBacktester

# Fetch real data
fetcher = HyperliquidDataFetcher()
df = fetcher.fetch_bitcoin_for_backtest(interval='1h', days_back=30)

# Run backtest
bt = BitcoinBacktester(initial_capital=10000, commission=0.001)
bt.data = df
bt.calculate_indicators()
metrics = bt.run_strategy('sma_crossover', allow_short=True)

# Analyze results
bt.print_performance_report(metrics)
bt.plot_results()
\`\`\`

## 🌐 24/7 Hosting

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for:
- DigitalOcean setup
- AWS EC2 deployment
- Automated scheduling
- Remote Jupyter access

## 📝 License

MIT License - See LICENSE file

## ⚠️ Disclaimer

This software is for educational purposes only. Past performance does not guarantee future results. Trading cryptocurrencies involves risk. Always do your own research.

## 🤝 Contributing

Pull requests welcome! Please read CONTRIBUTING.md first.

## 📧 Contact

- GitHub: [@$GITHUB_USER](https://github.com/$GITHUB_USER)
- Issues: [Report bugs](https://github.com/$GITHUB_USER/$REPO_NAME/issues)
EOF

echo "✅ README_GITHUB.md created"

# Add files
git add bitcoin_backtest.py
git add hyperliquid_data_fetcher.py
git add backtest_with_hyperliquid.py
git add simple_example.py
git add bitcoin_backtest_notebook.ipynb
git add README.md
git add README_GITHUB.md
git add HYPERLIQUID_GUIDE.md
git add QUICKSTART.md
git add DEPLOYMENT_GUIDE.md
git add requirements.txt
git add .gitignore

echo "✅ Files staged"

# Commit
git commit -m "Initial commit: Bitcoin backtesting system with Hyperliquid integration"

echo "✅ Initial commit created"

# Add remote
git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git" 2>/dev/null || \
git remote set-url origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "✅ Remote repository linked"

# Set branch name
git branch -M main

echo ""
echo "=================================="
echo "✅ Git setup complete!"
echo "=================================="
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Create the repository on GitHub:"
echo "   Go to: https://github.com/new"
echo "   Repository name: $REPO_NAME"
echo "   Click 'Create repository'"
echo ""
echo "2. Push your code:"
echo "   git push -u origin main"
echo ""
echo "3. Or, if you have GitHub CLI installed:"
echo "   gh repo create $REPO_NAME --public --source=. --push"
echo ""
echo "🔗 Your repository will be at:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
