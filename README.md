# cookie-clicker

A simple bot that automates clicking and purchasing in the popular game Cookie Clicker using Selenium.

## Demo

Watch the bot in action:

[![Cookie Clicker Bot Demo](assets/demo.gif)](https://www.youtube.com/watch?v=zXNmr61oR9Y)

Click the GIF above to watch the full video on YouTube!

## Introduction

Cookie Clicker Bot is a Python script that utilizes Selenium, a web automation library, to automate clicking and purchasing in the game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). The bot aims to maximize the player's progress and achieve higher scores by automating repetitive tasks.

For more information on installing Selenium, you can refer to the [Selenium installation documentation](https://selenium-python.readthedocs.io/installation.html#).

## Installation

1. Ensure you have Python installed on your machine. If not, you can download it from the [official Python website](https://www.python.org/).

2. Clone this repository to your local machine using the following command:

git clone https://github.com/raimonvibe/cookie-clicker.git

3. Navigate to the project directory:

cd cookie-clicker

4. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```
If you don't have the requirements.txt file, you can install the dependencies manually:
```bash
pip install selenium
```

6. Download the appropriate Selenium WebDriver for your browser and operating system:
- Download ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
- Make sure the ChromeDriver version matches your Chrome browser version

7. Set the path to the downloaded WebDriver in the `cookie_clicker_bot.py` script:
- Replace the `chrome_driver_path` variable with the path to your WebDriver executable
- On Windows, use double backslashes in the path (e.g., "C:\\path\\to\\chromedriver.exe")
- On Unix-based systems, use forward slashes (e.g., "/path/to/chromedriver")

## Features

- 🖱️ Automated cookie clicking
- 🛍️ Smart purchasing of upgrades and buildings
- ⚙️ Configurable clicking intervals
- 📊 Progress monitoring
- 🎮 Hands-free gameplay

## Usage

1. Make sure you have completed the installation steps.

2. On macOS, open Terminal and navigate to the project directory:

cd /path/to/cookie-clicker-bot

On Windows, open Command Prompt and navigate to the project directory:

cd C:\path\to\cookie-clicker-bot

3. Run the `cookie_clicker_bot.py` script:

python cookie_clicker_bot.py

4. The bot will open the Cookie Clicker game in a new browser window and start automating the clicking and purchasing process.

5. Sit back and watch as the bot plays Cookie Clicker for you!

## Configuration

The bot provides several configurable parameters that you can modify to customize its behavior. These parameters are located at the top of the `cookie_clicker_bot.py` script:

### Click Intervals
- `wait_duration`: Base clicking interval (in milliseconds) - controls how fast the bot clicks cookies
- `wait_duration2`: Upgrade purchase interval - determines how often the bot checks and buys available upgrades
- `wait_duration3`: Building purchase interval - sets the frequency of checking and purchasing new buildings

### Strategy Tips
- Lower values make the bot more aggressive in clicking and purchasing
- Higher values are more conservative and may be better for slower progression
- Recommended starting values:
  - wait_duration: 100 (clicks every 0.1 seconds)
  - wait_duration2: 1000 (checks upgrades every second)
  - wait_duration3: 2000 (checks buildings every 2 seconds)

## Troubleshooting

Common issues and solutions:

1. **ChromeDriver Version Mismatch**
   - Error: "This version of ChromeDriver only supports Chrome version XX"
   - Solution: Download the matching ChromeDriver version from the official website

2. **Selenium Installation Issues**
   - Make sure you're using a compatible Python version (3.6+)
   - Try upgrading pip: `pip install --upgrade pip`
   - Install Selenium in your virtual environment

3. **Bot Not Clicking**
   - Check if the game is properly loaded
   - Ensure the browser window is active and not minimized
   - Try increasing the wait durations

## License

This project is licensed under the [MIT License](LICENSE), which allows you to use, modify, and distribute the code freely. Please see the LICENSE file for more details.

---

**Disclaimer:** The Cookie Clicker Bot is an educational project and should be used responsibly. Automating gameplay in online games may violate the terms of service of the game.
