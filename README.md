# Slackmojis-Webscraper

## Usage
Solely used for scraping and uploading any GIF files not currently added to the specified Slack workspace.

## Instructions
1. [Download](https://chromedriver.chromium.org/downloads) the Chromedriver version compatible with your Chrome version.
    - Remember where you saved the executable.
2. [Install](https://www.python.org/downloads/) Python 3 if not already installed.
3. Install the required Python packages:
'pip3 install -r requirements.txt'
4. Get your xoxs Slack token using [this walkthrough](https://github.com/jackellenberger/emojme#finding-a-slack-token).
5. Execute the tool:
'python3 webscraper.py [--help] | [-d <chromedriver_path>] [-w <workspace_name>] [-t slack_token]'

### In Progess
- Scraping of other sites