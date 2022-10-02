# 🪙 Crypto Prices Bot for Telegram
Telegram bot that shows price of cryptocurrencies
[Try the my bot](https://t.me/CryptoPricesPBot)

About
------------
**A simple telegram bot that shows the price of cryptocurrencies. Used by the Cryptocompare API. The bot also works in group chats.**

Installation
------------
```shell
# Clone the repository
$ git clone https://github.com/onilyxe/CryptoPrices.git

# Change the working directory to CryptoPrices
$ cd CryptoPrices
```

Configuring
------------
**Open `config.yaml` configuration file with text editor and set the tokens and your id:**
```ini
TELEGRAM:
    API_KEY: 0000000000:0000000000000000000000000000000000
    LIST_OF_ADMINS:
        - 000000000
        - 000000001
CRYPTO:
  API_KEY: your-coinmarketcap-api_key
```
* `API_KEY` is token for your Telegram bot. You can get it here: [BotFather](https://t.me/BotFather)
* `LIST_OF_ADMINS` is list id

Running
------------
Using Python
```shell
# Install requirements
$ python3 -m pip install -r requirements.txt

# Run script
$ python3 bot.py
```