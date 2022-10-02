from plugins import new_message, enable_check
import cryptocompare
import currency

def btc(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return
    else:
        currency1 = "BTC"
        currency2 = "USD"
        symbol = currency.symbol(currency2, native=True)
        price = cryptocompare.get_price(currency1, currency=currency2, full=False)
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
        f"{symbol}*{price[currency1][currency2]}*")