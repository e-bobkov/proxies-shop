# Proxies Shop Telegram Bot

This project is a Telegram bot shop for purchasing proxies using the @CryptoPay payment system from @CryptoBot. The bot is written in Python 3.10 and utilizes the aiogram 3.x library.

## Features

- Purchase proxies directly through Telegram
- Secure payment processing with @CryptoPay from @CryptoBot
- User-friendly interface

## Requirements

- Python 3.10 or higher
- aiogram 3.x
- @CryptoPay account and API key

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/e-bobkov/proxies-shop.git
   cd proxies-shop
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root directory and add your Telegram bot token and CryptoPay API key:

   ```ini
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   CRYPTOPAY_API_KEY=your_cryptopay_api_key
   ```

## Usage

1. **Run the bot:**

   ```sh
   python bot.py
   ```

2. **Interact with the bot on Telegram:**

   Open your Telegram app, find your bot, and start interacting with it to purchase proxies.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to contribute.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [aiogram](https://github.com/aiogram/aiogram) for the Telegram bot framework
- [@CryptoPay](https://github.com/CryptoBot) for the payment system

```

Make sure to replace placeholders like `yourusername`, `your_telegram_bot_token`, and `your_cryptopay_api_key` with actual values relevant to your project. This README provides a comprehensive overview of your project, including features, installation instructions, usage, and contribution guidelines.
