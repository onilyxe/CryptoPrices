from plugins import new_message, enable_check
import cryptocompare
import currency
import requests
import yaml


def price(update, context):
    new_message.new_message(update)

    with open('config.yaml', 'r') as f:
        config = yaml.full_load(f)
        apikey = config['CRYPTO']['API_KEY']

    if enable_check.enable_check(__name__):
        return

    def changepct(time):
        if len(context.args) >= 2:
            currency1 = context.args[1]
        else:
            currency1 = "BTC"
        if len(context.args) == 3:
            currency2 = context.args[2]
        else:
            currency2 = "USD"
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY={apikey}&symbol={currency1.upper()}&convert={currency2.upper()}"
        r = requests.get(url)
        msg = r.json()['data'][currency1.upper()]['quote'][currency2.upper()][f'percent_change_{time[:-1]}']
        if msg > 0.01 or msg < -0.01:
            msg = round(msg, 2)
            if msg > 0.0:
                msg = f"+{msg}"
        return msg

    # /price 24h% BTC — изменения в цене за 24 часа в процентах (Имеется 3 аргумента: 24h%, 7d%, 30d%)
    if len(context.args) >= 1 and context.args[0] in ['24h%', '7d%', '30d%']:
        msg = changepct(context.args[0])
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
            f'*{msg}%*')

    # /price 24h BTC — изменения в цене за 24 часа (Можно указать вторую валюту: /price 24h BTC UAH. В таком случае изменения в цене будут показываться во второй валюте которую вы указали)
    elif len(context.args) >= 1 and context.args[0] == "24h":
        if len(context.args) >= 2:
            currency1 = context.args[1]
        else:
            currency1 = "BTC"
        if len(context.args) == 3:
            currency2 = context.args[2]
        else:
            currency2 = "USD"
        try:
            symbol = currency.symbol(currency2, native=True)
        except:
            symbol = ""
        avg = cryptocompare.get_avg(currency1, currency=currency2)
        msg = avg['CHANGE24HOUR']
        if msg > 0.01 or msg < -0.01:
            msg = round(msg, 2)
            if msg > 0.0:
                msg = f"+{msg}"
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
            f"*{msg}*{symbol}")

    # /price BTC UAH — краткая цена в в валюте которую вы указали второй
    elif len(context.args) >= 1:
        currency1 = context.args[0].upper()

        if len(context.args) == 2:
            currency2 = context.args[1].upper()
        else:
            currency2 = "USD"
        try:
            symbol = currency.symbol(currency2, native=True)
        except:
            symbol = ''
        price = cryptocompare.get_price(currency1, currency=currency2, full=False)

        if price:
            context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
                f"{symbol}*{price[currency1][currency2]}*")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
                f"ℹ️Не могу найти *{currency1}-{currency2}*\n🧑‍💻На всякий случай прочти /help")
        return

    elif not context.args or len(context.args) > 3:
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
            'ℹ️Не вижу нужных аргументов\n🧑‍💻На всякий случай прочти /help')
        return