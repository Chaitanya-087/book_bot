# Booking Bot

Automates IPL ticket booking on [district.in](https://www.district.in) using Robot Framework and Selenium. Opens Brave Browser with your saved session and clicks **Book Tickets** the instant it becomes available.

---

## Requirements

| Tool | Version |
|------|---------|
| macOS | Any (Apple Silicon supported) |
| Python | 3.10+ |
| Brave Browser | [brave.com/download](https://brave.com/download) |
| Homebrew | [brew.sh](https://brew.sh) |

---

## Setup

### 1. Clone / download the project

```bash
cd ~/Develop
# place the automation/ folder here
```

### 2. Create virtual environment and install dependencies

```bash
cd automation
python3 -m venv .venv
source .venv/bin/activate
pip install robotframework robotframework-seleniumlibrary selenium
```

### 3. Install ChromeDriver

Brave uses the Chromium engine — ChromeDriver is needed for Selenium to control it.

```bash
brew install chromedriver
# Remove macOS quarantine flag
xattr -d com.apple.quarantine $(which chromedriver)
```

### 4. Log in to district.in in Brave

1. Open **Brave Browser** normally
2. Go to [district.in](https://www.district.in)
3. Log in with your mobile number and OTP
4. **Stay logged in** — the bot reuses this session

> You only need to log in once. The session is preserved in your Brave profile.

---

## Usage

### Before every run

**Quit Brave completely** (Cmd+Q) — the profile cannot be used by two processes at once.

### Run the bot

```bash
cd ~/Develop/automation
source .venv/bin/activate
robot ipl_tickets/tests/book_tickets.robot
```

Brave opens, navigates to the match page, and clicks **Book Tickets** the moment it appears (polls continuously, up to 10 minutes).

### Change the match URL

Edit `ipl_tickets/tests/book_tickets.robot` and update `${MATCHURL}`:

```robot
${MATCHURL}    https://www.district.in/events/<your-match-slug>
```

---

## Project Structure

```
automation/
├── ipl_tickets/
│   ├── tests/
│   │   └── book_tickets.robot      # Main test — edit match URL here
│   ├── resources/
│   │   ├── keywords.robot          # Reusable keywords
│   │   └── BrowserSetup.py         # Brave session + Chrome options
│   └── session/
│       └── cookies.json            # Saved login cookies (auto-created)
├── results/                        # Robot Framework reports
└── .venv/                          # Python virtual environment
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `SessionNotCreatedException` | Brave is still running — quit it with Cmd+Q first |
| `SessionNotCreatedException: DevToolsActivePort` | Brave profile lock is stale — re-run, the bot clears it automatically |
| `chromedriver: command not found` | Run `brew install chromedriver` |
| `chromedriver` blocked by macOS | Run `xattr -d com.apple.quarantine $(which chromedriver)` |
| Bot opens but not logged in | Log in to district.in in Brave manually, then re-run |
| `Book Tickets` button never appears | Match URL may be wrong or sale hasn't started yet |
