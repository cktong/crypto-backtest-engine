#!/bin/bash
# Jupyter Notebook Startup Script
# ================================
# Starts Jupyter Notebook server for crypto backtesting

echo "🚀 Starting Jupyter Notebook Server..."
echo "=================================="
echo ""

# Change to the webapp directory
cd /home/user/webapp

# Start Jupyter Notebook
# Options:
#   --ip=0.0.0.0           : Allow connections from any IP
#   --port=8888            : Use port 8888 (default)
#   --no-browser           : Don't auto-open browser (for remote access)
#   --NotebookApp.token='' : No password (for development only)
#   --NotebookApp.password='' : No password
#   --allow-root           : Allow running as root if needed

echo "Starting Jupyter Notebook on port 8888..."
echo "Access it at: http://localhost:8888"
echo ""
echo "For remote access, use the public URL from GetServiceUrl tool"
echo "Press Ctrl+C to stop the server"
echo ""

jupyter notebook \
  --ip=0.0.0.0 \
  --port=8888 \
  --no-browser \
  --NotebookApp.token='' \
  --NotebookApp.password='' \
  --allow-root
