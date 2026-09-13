# Multi-Platform Fantasy Football Slack Notifier

An open-source Python script for Hermes Agent and the community that fetches fantasy matchup scores from **ESPN**, **Sleeper**, or **Yahoo** and pushes updates directly to a Slack channel via Webhooks.

---

## Supported Platforms & Configuration

Set `FANTASY_PLATFORM` to `espn`, `sleeper`, or `yahoo`, along with your platform-specific environment variables.

### Common Variables
| Environment Variable | Description | Example |
|----------------------|-------------|---|
| `FANTASY_PLATFORM`   | Platform to query (`espn`, `sleeper`, `yahoo`) | `espn` |
| `SLACK_WEBHOOK_URL`  | Incoming Webhook URL from Slack | `https://hooks.slack.com/services/...` |
| `FANTASY_TEAM_NAME`  | Your exact team name / owner name to track | `Lane's Johnson` |

---

### 1. ESPN Fantasy
| Environment Variable | Description | Example |
|----------------------|-------------|---|
| `ESPN_LEAGUE_ID`     | ESPN League ID | `754214` |
| `ESPN_YEAR`          | Season year | `2026` |
| `ESPN_S2`            | *(Private Leagues)* ESPN S2 cookie | `AE...` |
| `ESPN_SWID`          | *(Private Leagues)* ESPN SWID cookie | `{...}` |

---

### 2. Sleeper Fantasy
| Environment Variable | Description | Example |
|----------------------|-------------|---|
| `SLEEPER_LEAGUE_ID`  | Sleeper League ID | `123456789012345678` |

---

### 3. Yahoo Fantasy
Yahoo Fantasy requires OAuth authentication. You can plug in your Yahoo API credentials or use custom session tokens.

---

## Usage

```bash
export FANTASY_PLATFORM="espn"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
export ESPN_LEAGUE_ID="754214"
export FANTASY_TEAM_NAME="Lane's Johnson"
python3 fantasy_slack_notifier.py
```

---

## License
MIT License
