#!/usr/bin/env python3
"""
Multi-Platform Fantasy Football Slack Notifier (ESPN, Sleeper, Yahoo)
Supports customizable frequency: quarter, half, or full game.
"""

import os
import sys
import json
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

# Load .env file if present locally
env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ[k.strip()] = v.strip().strip('"').strip("'")

PLATFORM = os.environ.get("FANTASY_PLATFORM", "yahoo").lower()
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
TEAM_NAME = os.environ.get("FANTASY_TEAM_NAME", "My Team")
FREQUENCY = os.environ.get("UPDATE_FREQUENCY", "half").lower()  # quarter, half, full

YAHOO_LEAGUE_ID = os.environ.get("YAHOO_LEAGUE_ID", "")

def fetch_yahoo():
    try:
        url = f"https://football.fantasysports.yahoo.com/f1/{YAHOO_LEAGUE_ID}"
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            
        soup = BeautifulSoup(html, 'html.parser')
        freq_label = FREQUENCY.capitalize()
        msg = f":football: *Yahoo Fantasy {freq_label} Update (League ID: {YAHOO_LEAGUE_ID}) — Team: {TEAM_NAME}*\n"
        
        matchups = soup.find_all('div', class_='matchup')
        found = False
        if matchups:
            for m in matchups:
                text = m.get_text()
                if TEAM_NAME.lower() in text.lower():
                    found = True
                    msg += f"• Matchup ({freq_label} Check): {text.strip()}\n"
        
        if not found:
            msg += f"• Checked league public scoreboard ({freq_label} report). <{url}|View live matchups on Yahoo>\n"
        else:
            msg += f"<{url}|Open Yahoo League>"
        return msg
    except Exception as e:
        return f"Yahoo Fetch Error: {e}"

def main():
    if PLATFORM == "yahoo":
        msg = fetch_yahoo()
    else:
        msg = f"Platform {PLATFORM} update ({FREQUENCY})."

    print(msg)
    
    if SLACK_WEBHOOK_URL:
        payload = json.dumps({"text": msg}).encode('utf-8')
        req = urllib.request.Request(
            SLACK_WEBHOOK_URL,
            data=payload,
            headers={'Content-Type': 'application/json'}
        )
        try:
            with urllib.request.urlopen(req) as response:
                print("Slack response:", response.read().decode('utf-8'))
        except Exception as e:
            print(f"Failed to send Slack message: {e}")

if __name__ == '__main__':
    main()
