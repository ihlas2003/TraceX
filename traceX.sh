#!/bin/bash

echo "==================================================="
echo "⚙️  TraceX Auto-Installer & Launcher"
echo "==================================================="
echo "🔍 Required system packages-a install/check panrom..."

# Direct system packages automatic installation
pip install requests exifread folium pillow --break-system-packages

clear

echo -e "\n✅ All required modules are ready! Launching TraceX...\n"
sleep 1

# Tool-a launch 
python3 main.py
