# NFL-TailSlack 🏈

An open-source Python tool for Hermes Agent and the community that fetches fantasy matchup scores from **ESPN**, **Sleeper**, or **Yahoo** and pushes updates directly to a Slack channel via Webhooks.

---

## Quick Start for Non-Technical Users (Setup Wizard)

You don't need to manually edit configuration files. We provide an interactive setup wizard that walks you through everything and automatically creates your local `.env` file.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cmaloy12/nfl-tailslack.git
   cd nfl-tailslack
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the interactive setup wizard:**
   ```bash
   python3 fantasy_setup_wizard.py
   ```
   *The wizard will ask you for your platform (Yahoo, ESPN, Sleeper), team name, update frequency (quarter, half, full), league ID, and Slack Webhook URL—then automatically save them to `.env`.*

4. **Test your setup:**
   ```bash
   python3 fantasy_slack_notifier.py
   ```

---

## Supported Platforms & Configuration

### Common Settings (saved in `.env`)
| Variable | Description | Example |
|---|---|---|
| `FANTASY_PLATFORM` | Platform to query (`yahoo`, `espn`, `sleeper`) | `yahoo` |
| `FANTASY_TEAM_NAME` | Your exact team name to track | `Lane's Johnson` |
| `UPDATE_FREQUENCY` | Frequency (`quarter`, `half`, `full`) | `half` |
| `SLACK_WEBHOOK_URL` | Incoming Webhook URL from Slack | `https://hooks.slack.com/services/...` |

### Platform-Specific IDs
- **Yahoo:** `YAHOO_LEAGUE_ID` (e.g. `175960`)
- **ESPN:** `ESPN_LEAGUE_ID`, `ESPN_YEAR`, plus optional private league cookies (`ESPN_S2`, `ESPN_SWID`)
- **Sleeper:** `SLEEPER_LEAGUE_ID`

---

## License
MIT License
