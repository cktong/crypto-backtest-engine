# 🚀 Deployment Guide - 24/7 Hosting Options

Complete guide for hosting your Bitcoin backtesting system 24/7 with GitHub sync.

## 📋 Overview

Since you want to:
1. ✅ Run backtests 24/7 continuously
2. ✅ Edit code in Jupyter notebooks
3. ✅ Save changes automatically
4. ✅ Access from anywhere

**Best Solution**: Use **GitHub** for code storage + **Cloud hosting** for 24/7 execution

---

## 🔄 Part 1: GitHub Setup (Save Your Work)

### Why GitHub?
- ✅ Version control (track all changes)
- ✅ Cloud backup (never lose work)
- ✅ Access from anywhere
- ✅ Easy deployment to servers
- ✅ Collaboration ready

### Step 1: Create GitHub Repository

**Option A: Using GitHub Web Interface**
1. Go to https://github.com/new
2. Repository name: `bitcoin-backtest-hyperliquid`
3. Description: "Bitcoin backtesting system with Hyperliquid integration"
4. Choose "Public" or "Private"
5. Click "Create repository"

**Option B: Using GitHub CLI**
```bash
# Install GitHub CLI if needed
# Visit: https://cli.github.com/

# Login to GitHub
gh auth login

# Create repository
gh repo create bitcoin-backtest-hyperliquid --public --description "Bitcoin backtesting with Hyperliquid"
```

### Step 2: Push Your Code to GitHub

```bash
cd /home/user

# Initialize git repository
git init

# Create .gitignore file
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

# Data and results (don't commit generated files)
*.png
*.csv
*.log

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

# Add all your files
git add bitcoin_backtest.py
git add hyperliquid_data_fetcher.py
git add backtest_with_hyperliquid.py
git add simple_example.py
git add bitcoin_backtest_notebook.ipynb
git add README.md
git add HYPERLIQUID_GUIDE.md
git add QUICKSTART.md
git add DEPLOYMENT_GUIDE.md
git add .gitignore

# Commit
git commit -m "Initial commit: Bitcoin backtesting system with Hyperliquid integration"

# Link to your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/bitcoin-backtest-hyperliquid.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Future Updates

Whenever you make changes:
```bash
# Save changes
git add .
git commit -m "Updated strategy parameters"
git push

# Or use one command
git add . && git commit -m "Your change description" && git push
```

To pull changes on another machine:
```bash
git pull
```

---

## ☁️ Part 2: 24/7 Hosting Options

### **Option 1: DigitalOcean Droplet** ⭐ RECOMMENDED

**Best for**: Continuous backtesting, automated trading bots

**Pros:**
- ✅ Full control over environment
- ✅ Can run 24/7 reliably
- ✅ Affordable ($6-12/month)
- ✅ Easy setup

**Setup:**

1. **Create Droplet**
   - Go to https://www.digitalocean.com/
   - Create account (get $200 free credit)
   - Click "Create" → "Droplets"
   - Choose Ubuntu 22.04 LTS
   - Basic plan: $6/month (1GB RAM) or $12/month (2GB RAM)
   - Choose datacenter region near you

2. **Connect to Server**
   ```bash
   ssh root@YOUR_DROPLET_IP
   ```

3. **Install Python and Dependencies**
   ```bash
   # Update system
   apt update && apt upgrade -y
   
   # Install Python and pip
   apt install -y python3 python3-pip git
   
   # Install required packages
   pip3 install pandas numpy matplotlib requests jupyter
   ```

4. **Clone Your Repository**
   ```bash
   cd /root
   git clone https://github.com/YOUR_USERNAME/bitcoin-backtest-hyperliquid.git
   cd bitcoin-backtest-hyperliquid
   ```

5. **Run Continuously**
   ```bash
   # Option A: Run once
   python3 backtest_with_hyperliquid.py
   
   # Option B: Run every hour (scheduled)
   # Create cron job
   crontab -e
   # Add this line:
   # 0 * * * * cd /root/bitcoin-backtest-hyperliquid && python3 backtest_with_hyperliquid.py >> backtest.log 2>&1
   ```

6. **Access Jupyter Notebook Remotely**
   ```bash
   # Install Jupyter
   pip3 install jupyter
   
   # Start Jupyter with remote access
   jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
   
   # Access from your computer:
   # http://YOUR_DROPLET_IP:8888
   # Use the token from terminal output
   ```

**Cost**: $6-12/month

---

### **Option 2: AWS EC2 Free Tier** 💰 FREE (1 year)

**Best for**: Testing and learning

**Pros:**
- ✅ Free for 12 months
- ✅ 750 hours/month (enough for 24/7)
- ✅ Industry standard

**Setup:**

1. **Create AWS Account**
   - Go to https://aws.amazon.com/free/
   - Sign up (requires credit card, but won't charge for free tier)

2. **Launch EC2 Instance**
   - Go to EC2 Dashboard
   - Click "Launch Instance"
   - Name: `bitcoin-backtest`
   - AMI: Ubuntu Server 22.04 LTS
   - Instance type: t2.micro (free tier)
   - Create new key pair (download .pem file)
   - Security group: Allow SSH (port 22) and Custom TCP (port 8888 for Jupyter)
   - Launch instance

3. **Connect**
   ```bash
   chmod 400 your-key.pem
   ssh -i your-key.pem ubuntu@YOUR_EC2_IP
   ```

4. **Install and Run** (same as DigitalOcean steps 3-6)

**Cost**: FREE for 12 months, then ~$8/month

---

### **Option 3: Google Cloud (Compute Engine)** 💰 FREE ($300 credit)

**Best for**: Heavy computation needs

**Pros:**
- ✅ $300 free credit (3 months)
- ✅ Powerful machines available
- ✅ Good for data-intensive work

**Setup:**

1. **Create GCP Account**
   - Go to https://cloud.google.com/free
   - Sign up (get $300 free credit)

2. **Create VM Instance**
   - Go to Compute Engine → VM instances
   - Click "Create Instance"
   - Name: `bitcoin-backtest`
   - Region: Choose nearest
   - Machine type: e2-micro (free tier) or e2-small
   - Boot disk: Ubuntu 22.04 LTS
   - Allow HTTP/HTTPS traffic
   - Create

3. **Connect and Setup** (similar to previous options)

**Cost**: FREE with $300 credit, then ~$7/month

---

### **Option 4: Oracle Cloud Free Tier** 💰 FREE (Forever)

**Best for**: Budget-conscious, permanent free hosting

**Pros:**
- ✅ Always free (no time limit)
- ✅ Decent specs (1GB RAM, 1 CPU)
- ✅ No credit card required after trial

**Setup:**

1. Go to https://www.oracle.com/cloud/free/
2. Create account
3. Create Compute Instance (ARM Ampere or AMD)
4. Follow similar setup as DigitalOcean

**Cost**: FREE forever

---

### **Option 5: Raspberry Pi** (Local 24/7)

**Best for**: Home server, learning

**Pros:**
- ✅ One-time cost (~$50-100)
- ✅ No monthly fees
- ✅ Full control
- ✅ Low power consumption

**Setup:**

1. Buy Raspberry Pi 4 (4GB+ RAM recommended)
2. Install Raspberry Pi OS
3. Clone your repository
4. Run scripts

**Cons:**
- ❌ Requires physical hardware
- ❌ Depends on home internet
- ❌ Less reliable than cloud

**Cost**: $50-100 one-time

---

### **Option 6: Replit** (Quick & Easy)

**Best for**: Quick testing, no server management

**Pros:**
- ✅ Free tier available
- ✅ No setup required
- ✅ Built-in code editor

**Setup:**

1. Go to https://replit.com
2. Create new Repl (Python)
3. Upload your files or import from GitHub
4. Click "Run"

**Cons:**
- ❌ Limited free hours
- ❌ Not ideal for 24/7
- ❌ Less powerful

**Cost**: FREE (limited), $7/month (unlimited)

---

## 🎯 Recommended Setup for Your Use Case

### **Best Choice: DigitalOcean + GitHub**

Here's why:
1. ✅ **Reliable 24/7** hosting
2. ✅ **Easy to manage**
3. ✅ **Affordable** ($6-12/month)
4. ✅ **Jupyter notebook** support
5. ✅ **GitHub integration** for code sync

### Complete Workflow:

#### On Your Local Machine (Development)
```bash
# 1. Make changes to code/notebook
# Edit files in Jupyter notebook or VS Code

# 2. Save to GitHub
git add .
git commit -m "Updated strategy"
git push
```

#### On DigitalOcean Server (Production)
```bash
# 1. Pull latest changes
cd /root/bitcoin-backtest-hyperliquid
git pull

# 2. Run backtest
python3 backtest_with_hyperliquid.py

# 3. Or run continuously with cron
# Runs every hour automatically
```

#### Access Jupyter Remotely
```bash
# On server:
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# On your computer:
# Open browser: http://YOUR_SERVER_IP:8888
# Edit notebooks directly on the server!
```

---

## 🔒 Security Best Practices

### 1. Use SSH Keys (Not Passwords)
```bash
# Generate SSH key on your computer
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy to server
ssh-copy-id root@YOUR_SERVER_IP

# Disable password login on server
# Edit /etc/ssh/sshd_config
# Set: PasswordAuthentication no
# Restart: systemctl restart sshd
```

### 2. Set Up Firewall
```bash
# On server
ufw allow 22/tcp    # SSH
ufw allow 8888/tcp  # Jupyter (optional)
ufw enable
```

### 3. Use Environment Variables for Secrets
```bash
# Create .env file (never commit to GitHub)
echo "API_KEY=your_key_here" > .env

# In Python:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('API_KEY')
```

### 4. Set Jupyter Password
```bash
# On server
jupyter notebook password
# Enter password when prompted
```

---

## 🔄 Automated Deployment Workflow

### Create Deployment Script

```bash
# Create deploy.sh
cat > /root/bitcoin-backtest-hyperliquid/deploy.sh << 'EOF'
#!/bin/bash

# Pull latest code
cd /root/bitcoin-backtest-hyperliquid
git pull

# Install/update dependencies
pip3 install -r requirements.txt

# Run backtest
python3 backtest_with_hyperliquid.py

# Send notification (optional)
echo "Backtest completed at $(date)" | mail -s "Backtest Update" your@email.com
EOF

chmod +x deploy.sh
```

### Schedule with Cron

```bash
# Edit crontab
crontab -e

# Add these lines:

# Run backtest every hour
0 * * * * /root/bitcoin-backtest-hyperliquid/deploy.sh >> /var/log/backtest.log 2>&1

# Pull GitHub updates every 5 minutes
*/5 * * * * cd /root/bitcoin-backtest-hyperliquid && git pull >> /var/log/git-pull.log 2>&1

# Daily summary at 9 AM
0 9 * * * python3 /root/bitcoin-backtest-hyperliquid/generate_report.py
```

---

## 📊 Monitoring Your 24/7 System

### 1. Check Logs
```bash
# View recent backtest results
tail -f /var/log/backtest.log

# View cron execution
tail -f /var/log/syslog | grep CRON
```

### 2. Create Monitoring Script

```python
# monitoring.py
import psutil
import requests
from datetime import datetime

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    print(f"[{datetime.now()}]")
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")
    print(f"Disk: {disk}%")
    
    # Alert if high usage
    if cpu > 90 or ram > 90 or disk > 90:
        send_alert(f"High resource usage! CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%")

def send_alert(message):
    # Send to Discord, Telegram, email, etc.
    print(f"ALERT: {message}")

if __name__ == "__main__":
    check_system_health()
```

### 3. Set Up Alerts

Use services like:
- **UptimeRobot** (free): Monitor if server goes down
- **Better Stack** (free tier): Log aggregation
- **Discord webhook**: Real-time notifications

---

## 💾 Backup Strategy

### Automatic Backups to GitHub

```bash
# Create backup script
cat > /root/bitcoin-backtest-hyperliquid/backup.sh << 'EOF'
#!/bin/bash

cd /root/bitcoin-backtest-hyperliquid

# Backup results
mkdir -p backups
cp *.csv *.png backups/
tar -czf backups/results-$(date +%Y%m%d).tar.gz backups/*.csv backups/*.png

# Commit results (optional)
git add backups/
git commit -m "Backup: $(date)"
git push

echo "Backup completed at $(date)"
EOF

chmod +x backup.sh

# Run daily at midnight
# Add to crontab:
# 0 0 * * * /root/bitcoin-backtest-hyperliquid/backup.sh
```

---

## 🎓 Complete Setup Example

### From Zero to Running 24/7

```bash
# 1. ON YOUR LOCAL MACHINE

# Create GitHub repository
gh repo create bitcoin-backtest-hyperliquid --public

# Push code
cd /home/user
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/bitcoin-backtest-hyperliquid.git
git push -u origin main

# 2. ON DIGITALOCEAN

# Create droplet (via web interface)
# Then SSH in:
ssh root@YOUR_DROPLET_IP

# Setup environment
apt update && apt upgrade -y
apt install -y python3 python3-pip git
pip3 install pandas numpy matplotlib requests jupyter

# Clone repository
git clone https://github.com/YOUR_USERNAME/bitcoin-backtest-hyperliquid.git
cd bitcoin-backtest-hyperliquid

# Run initial test
python3 backtest_with_hyperliquid.py

# Setup automated runs
crontab -e
# Add: 0 * * * * cd /root/bitcoin-backtest-hyperliquid && python3 backtest_with_hyperliquid.py >> /var/log/backtest.log 2>&1

# Start Jupyter (for editing)
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# 3. ON YOUR COMPUTER

# Access Jupyter notebook
# Open browser: http://YOUR_DROPLET_IP:8888
# Edit notebooks directly!

# Make changes, save, and push to GitHub
git add .
git commit -m "Updated parameters"
git push

# Server automatically pulls and runs updated code
```

---

## 💰 Cost Comparison

| Option | Setup Time | Monthly Cost | Free Period | Best For |
|--------|-----------|--------------|-------------|----------|
| **DigitalOcean** | 10 min | $6-12 | $200 credit | Most users ⭐ |
| **AWS EC2** | 15 min | FREE → $8 | 12 months | Learning |
| **Google Cloud** | 15 min | FREE → $7 | $300 credit | Heavy compute |
| **Oracle Cloud** | 20 min | FREE | Forever | Budget users |
| **Raspberry Pi** | 1 hour | $0 | N/A | DIY/Local |
| **Replit** | 5 min | $0-7 | Limited | Quick tests |

---

## 🚀 Quick Start Recommendation

**For immediate 24/7 hosting:**

1. **Use DigitalOcean** ($200 free credit = ~30 months free)
   - Sign up: https://www.digitalocean.com/
   - Create $6/month droplet
   - Takes 10 minutes to setup

2. **Push to GitHub** (free code storage + sync)
   - Create repository
   - Push your code
   - Edit anywhere, sync everywhere

3. **Access remotely**
   - SSH for command line
   - Jupyter for notebook editing
   - GitHub for version control

**Total setup time**: ~30 minutes  
**Total cost**: FREE for ~30 months with credits

---

## ✅ Next Steps

1. Choose your hosting platform
2. Create GitHub repository
3. Deploy your code
4. Set up automated runs
5. Start Jupyter for remote editing
6. Monitor and iterate!

You'll have a professional 24/7 backtesting system with full version control and remote access! 🎉
