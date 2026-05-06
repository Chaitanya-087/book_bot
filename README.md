# Booking Bot

Automates IPL ticket booking on [district.in](https://www.district.in) using Robot Framework and Selenium. Opens Brave Browser with your saved session and clicks **Book Tickets** the instant it becomes available.

---

## Requirements

| Tool | Notes |
| ---- | ----- |
| Python 3.10+ | [python.org/downloads](https://www.python.org/downloads) |
| Brave Browser | [brave.com/download](https://brave.com/download) |
| ChromeDriver | Installed via steps below |

---

## Setup — macOS

### 1. Place the project

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

```bash
brew install chromedriver
# Remove macOS quarantine flag
xattr -d com.apple.quarantine $(which chromedriver)
```

> If you don't have Homebrew: [brew.sh](https://brew.sh)

### 4. Log in to district.in in Brave

1. Open **Brave Browser** normally
2. Go to [district.in](https://www.district.in)
3. Log in with your mobile number and OTP
4. **Stay logged in** — the bot reuses this session

> You only need to log in once. The session is preserved in your Brave profile.

### 5. Run the bot

**Quit Brave completely first** (Cmd+Q), then:

```bash
cd ~/Develop/automation
source .venv/bin/activate
robot ipl_tickets/tests/book_tickets.robot
```

---

## Setup — Windows

### 1. Install Python

Download and install Python 3.10+ from [python.org/downloads](https://www.python.org/downloads).

During installation, check **"Add Python to PATH"**.

Verify in Command Prompt:

```cmd
python --version
```

### 2. Place the project

```cmd
cd %USERPROFILE%\Develop
:: place the automation\ folder here
```

### 3. Create virtual environment and install dependencies

```cmd
cd automation
python -m venv .venv
.venv\Scripts\activate
pip install robotframework robotframework-seleniumlibrary selenium
```

### 4. Install ChromeDriver

Selenium Manager (bundled with Selenium 4.10+) downloads ChromeDriver automatically — no manual install needed on Windows.

If it fails, download the matching version manually from [googlechromelabs.github.io/chrome-for-testing](https://googlechromelabs.github.io/chrome-for-testing/) and place `chromedriver.exe` in the project root or anywhere on your `PATH`.

### 5. Update Brave profile path in BrowserSetup.py

Open `ipl_tickets/resources/BrowserSetup.py` and update the path for Windows:

```python
BRAVE_BINARY = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
BRAVE_PROFILE_DIR = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\BraveSoftware\Brave-Browser\User Data"
```

### 6. Log in to district.in in Brave

1. Open **Brave Browser** normally
2. Go to [district.in](https://www.district.in)
3. Log in with your mobile number and OTP
4. **Stay logged in** — the bot reuses this session

### 7. Run the bot

**Close Brave completely first** (right-click taskbar icon → Quit), then open Command Prompt:

```cmd
cd %USERPROFILE%\Develop\automation
.venv\Scripts\activate
robot ipl_tickets/tests/book_tickets.robot
```

---

## Change the Match URL

Edit `ipl_tickets/tests/book_tickets.robot` and update `${MATCHURL}`:

```robot
${MATCHURL}    https://www.district.in/events/<your-match-slug>
```

---

## Project Structure

```text
automation/
├── ipl_tickets/
│   ├── tests/
│   │   └── book_tickets.robot      # Main test — edit match URL here
│   ├── resources/
│   │   ├── keywords.robot          # Reusable keywords
│   │   └── BrowserSetup.py         # Brave session + Chrome options
│   └── session/
├── results/                        # Robot Framework reports
└── .venv/                          # Python virtual environment
```

---

## Troubleshooting

| Error | Fix |
| ----- | --- |
| `SessionNotCreatedException` | Brave is still running — quit it fully before running |
| `DevToolsActivePort file doesn't exist` | Brave profile lock is stale — re-run, the bot clears it automatically |
| `chromedriver: command not found` (macOS) | Run `brew install chromedriver` |
| `chromedriver` blocked by macOS | Run `xattr -d com.apple.quarantine $(which chromedriver)` |
| Bot opens but not logged in | Log in to district.in in Brave manually, then re-run |
| `Book Tickets` button never appears | Match URL may be wrong or sale hasn't started yet |
| `[WinError 2]` chromedriver not found (Windows) | Place `chromedriver.exe` in the project root or on `PATH` |
