from plugins import new_message, enable_check
import cryptocompare
import currency


def p(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    elif len(context.args) >= 1:
        currency1 = context.args[0].upper()
        currency2 = "USD"
        EUR = "EUR"
        UAH = "UAH"
        RUB = "RUB"
        try:
            symbol = currency.symbol(currency2, native=True)
            sEUR = currency.symbol(EUR, native=True)
            sUAH = currency.symbol(UAH, native=True)
            sRUB = currency.symbol(RUB, native=False)
        except:
            symbol = ''
        price = cryptocompare.get_price(currency1, currency=currency2, full=False)
        pEUR = cryptocompare.get_price(currency1, currency=EUR, full=False)
        pUAH = cryptocompare.get_price(currency1, currency=UAH, full=False)
        pRUB = cryptocompare.get_price(currency1, currency=RUB, full=False)

        if price:
            context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=            
            f"— _{currency1}:_"+
            f"\n— {symbol}*{price[currency1][currency2]}*"+
            f"\n— {sEUR}*{pEUR[currency1][EUR]}*"+
            f"\n— {sUAH}*{pUAH[currency1][UAH]}*"+
            f"\n— {sRUB}*{pRUB[currency1][RUB]}*")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
                f"ℹ️Не могу найти *{currency1}-{currency2}*\n🧑‍💻На всякий случай прочти /help")
        return

    elif not context.args or len(context.args) > 3:
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
            'ℹ️Не вижу нужных аргументов\n🧑‍💻На всякий случай прочти /help')
        return