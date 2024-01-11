# Discord Link Opener

Automatically open browser tabs when links matching given constraints are sent in Discord channels.

**Note:** discord.py updates have deprecated the previous version of this script. To run it now, you must install discord.py-self.

## Installation and Usage

> Link must be in URL format (protocol, domain name, and path).

1. Download [Python 3.6.x or higher](https://www.python.org/downloads/). Before installing, make sure to check “Add Python to PATH”.

2. Once installed, open CMD and type:

   ```bash
   pip install discord.py-self
   pip install asyncio
   git clone https://github.com/dolfies/discord.py-self
   cd discord.py-self
   python3 -m pip install -U .
   ```

---

3. Download and run [diswatcher.exe](https://github.com/anishBudha/diswatcher/releases/download/v0.1.1/diswatcher.exe) - click to download.
   > OR
4. Download Files from github.

5. Run `open.py` and follow the prompts:

   - **Step 1:** Enter your Discord token. ([Watch this video to know how to get your Discord token](https://www.youtube.com/watch?v=YEgFvgg7ZPI&ab_channel=GaugingGadgets))
   - **Step 2:** Enter Discord channel IDs (separated by commas) that you would like to monitor. (To get channeld id, right click on the channel name and select copy id)

   - **Step 3:** Enter whitelisted words (keywords) in lowercase, separated by spaces.
   - **Step 4:** Enter blacklisted words in lowercase, separated by spaces.

   **Note:** Do not edit the keyword and blacklist lines in the code.

6. Save the file.

7. Run `open.py`, and the bot will automatically open Chrome browser tabs when links matching given constraints are sent in the specified Discord channels.

8. To change keywords at any point, press `Ctrl + c` to terminate the script. Then simply run the script again and enter new words when prompted.

## Requirements

- asyncio
- discord.py-self
- keyborad

## Operating Systems

This was designed for and only tested on Windows.
