#!/usr/bin/env python3
import os
import json
import urllib.request
from bs4 import BeautifulSoup

def get_nfl_fantasy_news():
    try:
        url = "https://www.espn.com/nfl/"
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        
        for item in soup.find_all(['span', 'h2', 'h3'], class_=['contentItem__title', 'headline'], limit=15):
            text = item.get_text().strip()
            if text and len(text) > 10 and text not in headlines:
                headlines.append(text)
                
        if not headlines:
            # Fallback to general h2/h3
            for item in soup.find_all(['h2', 'h3'], limit=15):
                text = item.get_text().strip()
                if text and len(text) > 10 and text not in headlines:
                    headlines.append(text)

        msg = ":newspaper: *Latest NFL & Fantasy News*\n"
        for h in headlines[:5]:
            msg += f"• {h}\n"
            
        msg += f"\n<https://www.espn.com/nfl/|View ESPN NFL>"
        return msg
    except Exception as e:
        return f":newspaper: *Fantasy News Update Error:* {e}"

def main():
    msg = get_nfl_fantasy_news()
    print(msg)
    
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL', '')
    if webhook_url:
        payload = json.dumps({"text": msg}).encode('utf-8')
        req = urllib.request.Request(
            webhook_url,
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
