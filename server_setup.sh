#!/bin/bash

# Server Setup Script for 24/7 Hosting
# Run this on your DigitalOcean/AWS/GCP server after SSH login

echo "=================================="
echo "Bitcoin Backtest Server Setup"
echo "=================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Please run as root (sudo bash server_setup.sh)"
    exit 1
fi

echo "This script will:"
echo "  1. Update system packages"
echo "  2. Install Python and dependencies"
echo "  3. Clone your GitHub repository"
echo "  4. Set up automated backtesting"
echo "  5. Configure Jupyter for remote access"
echo ""

read -p "Continue? (y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "📦 Step 1: Updating system packages..."
apt update && apt upgrade -y
echo "✅ System updated"

echo ""
echo "🐍 Step 2: Installing Python and tools..."
apt install -y python3 python3-pip git vim htop
echo "✅ Python installed"

echo ""
echo "📚 Step 3: Installing Python packages..."
pip3 install pandas numpy matplotlib requests jupyter notebook
echo "✅ Python packages installed"

echo ""
echo "📥 Step 4: Cloning GitHub repository..."
read -p "Enter your GitHub username: " GITHUB_USER
read -p "Enter repository name (default: bitcoin-backtest-hyperliquid): " REPO_NAME
REPO_NAME=${REPO_NAME:-bitcoin-backtest-hyperliquid}

cd /root
git clone "https://github.com/$GITHUB_USER/$REPO_NAME.git"

if [ $? -eq 0 ]; then
    echo "✅ Repository cloned successfully"
    cd "/root/$REPO_NAME"
else
    echo "❌ Failed to clone repository. Please check the URL and try again."
    exit 1
fi

echo ""
echo "🧪 Step 5: Testing installation..."
python3 -c "
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import requests
print('✅ All imports successful')
"

if [ $? -ne 0 ]; then
    echo "❌ Import test failed. Please check error messages above."
    exit 1
fi

echo ""
echo "🎯 Step 6: Running initial backtest..."
python3 simple_example.py

echo ""
echo "⏰ Step 7: Setting up automated scheduling..."
echo "How often should backtests run?"
echo "  1) Every hour"
echo "  2) Every 4 hours"
echo "  3) Every 6 hours"
echo "  4) Once daily"
echo "  5) Skip automated setup"
read -p "Choose (1-5): " SCHEDULE_CHOICE

case $SCHEDULE_CHOICE in
    1)
        CRON_SCHEDULE="0 * * * *"
        SCHEDULE_DESC="every hour"
        ;;
    2)
        CRON_SCHEDULE="0 */4 * * *"
        SCHEDULE_DESC="every 4 hours"
        ;;
    3)
        CRON_SCHEDULE="0 */6 * * *"
        SCHEDULE_DESC="every 6 hours"
        ;;
    4)
        CRON_SCHEDULE="0 9 * * *"
        SCHEDULE_DESC="daily at 9 AM"
        ;;
    5)
        echo "Skipping automated setup"
        SCHEDULE_CHOICE=""
        ;;
    *)
        echo "Invalid choice, skipping automated setup"
        SCHEDULE_CHOICE=""
        ;;
esac

if [ -n "$SCHEDULE_CHOICE" ] && [ "$SCHEDULE_CHOICE" != "5" ]; then
    # Create cron job
    CRON_JOB="$CRON_SCHEDULE cd /root/$REPO_NAME && python3 backtest_with_hyperliquid.py >> /var/log/backtest.log 2>&1"
    
    # Add to crontab
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    
    # Also add GitHub pull job to stay updated
    PULL_JOB="*/10 * * * * cd /root/$REPO_NAME && git pull >> /var/log/git-pull.log 2>&1"
    (crontab -l 2>/dev/null; echo "$PULL_JOB") | crontab -
    
    echo "✅ Automated backtesting configured ($SCHEDULE_DESC)"
    echo "✅ GitHub auto-pull configured (every 10 minutes)"
fi

echo ""
echo "📓 Step 8: Setting up Jupyter Notebook..."
read -p "Set up Jupyter for remote access? (y/n): " JUPYTER_SETUP

if [ "$JUPYTER_SETUP" = "y" ]; then
    echo "Setting Jupyter password..."
    jupyter notebook password
    
    # Create systemd service for Jupyter
    cat > /etc/systemd/system/jupyter.service << EOF
[Unit]
Description=Jupyter Notebook Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/$REPO_NAME
ExecStart=/usr/local/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
Restart=always

[Install]
WantedBy=multi-user.target
EOF
    
    # Enable and start service
    systemctl daemon-reload
    systemctl enable jupyter
    systemctl start jupyter
    
    echo "✅ Jupyter configured and started"
    echo ""
    echo "🔒 Configuring firewall..."
    
    # Setup UFW firewall
    ufw allow 22/tcp    # SSH
    ufw allow 8888/tcp  # Jupyter
    ufw --force enable
    
    echo "✅ Firewall configured"
fi

echo ""
echo "🎨 Step 9: Creating management scripts..."

# Create update script
cat > /root/$REPO_NAME/update.sh << 'UPDATEEOF'
#!/bin/bash
echo "Updating Bitcoin Backtest System..."
cd /root/bitcoin-backtest-hyperliquid
git pull
pip3 install -r requirements.txt
echo "✅ Update complete!"
UPDATEEOF

chmod +x /root/$REPO_NAME/update.sh

# Create status script
cat > /root/$REPO_NAME/status.sh << 'STATUSEOF'
#!/bin/bash
echo "=================================="
echo "Bitcoin Backtest System Status"
echo "=================================="
echo ""
echo "📊 Recent Backtest Logs:"
tail -20 /var/log/backtest.log
echo ""
echo "🔄 Git Pull Status:"
tail -5 /var/log/git-pull.log
echo ""
echo "💻 System Resources:"
echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')% used"
echo "RAM: $(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2}')"
echo "Disk: $(df -h / | awk 'NR==2{print $5}')"
echo ""
echo "📓 Jupyter Status:"
systemctl status jupyter --no-pager -l | grep "Active:"
echo ""
echo "⏰ Scheduled Jobs:"
crontab -l | grep -v "^#"
STATUSEOF

chmod +x /root/$REPO_NAME/status.sh

# Create restart script
cat > /root/$REPO_NAME/restart.sh << 'RESTARTEOF'
#!/bin/bash
echo "Restarting Bitcoin Backtest Services..."
systemctl restart jupyter
echo "✅ Jupyter restarted"
RESTARTEOF

chmod +x /root/$REPO_NAME/restart.sh

echo "✅ Management scripts created"

echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "📋 Server Information:"
echo "   IP Address: $(hostname -I | awk '{print $1}')"
echo "   Repository: /root/$REPO_NAME"
echo ""
echo "🎯 Quick Commands:"
echo "   Check status:    /root/$REPO_NAME/status.sh"
echo "   Update code:     /root/$REPO_NAME/update.sh"
echo "   Restart Jupyter: /root/$REPO_NAME/restart.sh"
echo "   View logs:       tail -f /var/log/backtest.log"
echo ""

if [ "$JUPYTER_SETUP" = "y" ]; then
    SERVER_IP=$(hostname -I | awk '{print $1}')
    echo "📓 Jupyter Notebook:"
    echo "   URL: http://$SERVER_IP:8888"
    echo "   Use the password you set above"
    echo ""
fi

if [ -n "$SCHEDULE_CHOICE" ] && [ "$SCHEDULE_CHOICE" != "5" ]; then
    echo "⏰ Automated Backtesting:"
    echo "   Schedule: $SCHEDULE_DESC"
    echo "   Logs: /var/log/backtest.log"
    echo ""
fi

echo "🔒 Security Reminder:"
echo "   - Consider setting up SSH keys"
echo "   - Keep system updated: apt update && apt upgrade"
echo "   - Monitor logs regularly"
echo ""
echo "🚀 Your 24/7 backtesting system is ready!"
echo ""
