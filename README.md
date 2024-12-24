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

git clone https://github.com/your-username/cookie-clicker-bot.git

3. Navigate to the project directory:

cd cookie-clicker-bot

4. Install the required dependencies. If you don't have a requirements file, you can install Selenium using pip:

pip install selenium

5. Download the appropriate Selenium WebDriver for your browser and operating system.
- Download the ChromeDriver from (https://selenium-python.readthedocs.io/installation.html)

6. Set the path to the downloaded WebDriver in the `cookie_clicker_bot.py` script. Replace the `chrome_driver_path` variable with the path to the WebDriver executable.

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

The bot provides several configurable parameters that you can modify to customize its behavior. These parameters are located at the top of the `cookie_clicker_bot.py` script and include:

- `wait_duration`: The number of clicks the bot will perform before purchasing a specific product.
- `wait_duration2`: The number of clicks the bot will perform before purchasing the next product.
- `wait_duration3`: The number of clicks the bot will perform before purchasing the final product.

Feel free to adjust these values to fine-tune the bot's strategy based on your preferences.

## License

This project is licensed under the [MIT License](LICENSE), which allows you to use, modify, and distribute the code freely. Please see the LICENSE file for more details.

---

**Disclaimer:** The Cookie Clicker Bot is an educational project and should be used responsibly. Automating gameplay in online games may violate the terms of service of the game.
