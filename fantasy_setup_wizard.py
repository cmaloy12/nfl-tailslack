#!/usr/bin/env python3
"""
Interactive Setup Wizard for Fantasy Football Slack Notifier.
Walks the user through platform selection, league credentials, and Slack webhook configuration.
"""

import os
import sys

def prompt(question, default=""):
    resp = input(f"{question} [{default}]: ").strip()
    return resp if resp else default

def main():
    print("==================================================")
    print("  Fantasy Football Slack Notifier - Setup Wizard  ")
    print("==================================================")
    print("This wizard will help you configure your daily/halftime updates.\n")
    
    # 1. Platform selection
    print("Select your fantasy platform:")
    print("  1) ESPN")
    print("  2) Sleeper")
    print("  3) Yahoo")
    choice = prompt("Enter choice (1-3)", "1")
    
    platform_map = {"1": "espn", "2": "sleeper", "3": "yahoo"}
    platform = platform_map.get(choice, "espn")
    
    # 2. Team Name
    team_name = prompt("Enter your exact fantasy team name", "Lane's Johnson")
    
    # 3. Slack Webhook URL
    webhook_url = prompt("Enter your Slack Incoming Webhook URL", "https://hooks.slack.com/services/...")
    
    # 4. Platform specific credentials
    config_lines = [
        f"export FANTASY_PLATFORM=\"{platform}\"",
        f"export FANTASY_TEAM_NAME=\"{team_name}\"",
        f"export SLACK_WEBHOOK_URL=\"{webhook_url}\""
    ]
    
    if platform == "espn":
        league_id = prompt("Enter your ESPN League ID", "754214")
        year = prompt("Enter season year", "2026")
        config_lines.append(f"export ESPN_LEAGUE_ID=\"{league_id}\"")
        config_lines.append(f"export ESPN_YEAR=\"{year}\"")
        
        private = prompt("Is your ESPN league private? (y/n)", "n")
        if private.lower() == 'y':
            espn_s2 = prompt("Enter ESPN S2 cookie value")
            swid = prompt("Enter ESPN SWID cookie value")
            config_lines.append(f"export ESPN_S2=\"{espn_s2}\"")
            config_lines.append(f"export ESPN_SWID=\"{swid}\"")
            
    elif platform == "sleeper":
        sleeper_league_id = prompt("Enter your Sleeper League ID")
        config_lines.append(f"export SLEEPER_LEAGUE_ID=\"{sleeper_league_id}\"")
        
    elif platform == "yahoo":
        print("\nNote: Yahoo requires API keys or OAuth setup.")
        
    # Save to a local .env file
    env_path = os.path.expanduser("~/.hermes/fantasy_config.env")
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    with open(env_path, "w") as f:
        f.write("\n".join(config_lines) + "\n")
        
    print("\n==================================================")
    print(f"Setup complete! Configuration saved to: {env_path}")
    print("You can test your notifier by running:")
    print(f"  source {env_path} && python3 fantasy_slack_notifier.py")
    print("==================================================")

if __name__ == "__main__":
    main()
