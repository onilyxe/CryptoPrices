from plugins import new_message, enable_chec


def help(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "⚙️*Список команд:*"+
    "\n*/start* — _запустить бота._"+
    "\n*/help* — _это сообщение._"+
    "\n*/btc* — _краткая цена BTC в $_"+
    "\n*/pbtc* — _цена BTC в 4-х валютах. (USD, EUR, UAH, RUB)_"+
    "\n*/p BTC* — _показывает цену в 4-х валютах. (USD, EUR, UAH, RUB)_"+
    "\n*/price* — _узнать цену валюты. Имеет разные аргументы которые указаны ниже._"+
    "\n\n🛠*Доступные аргументы:*"+
    "\n*/price BTC* — _краткая цена в $_"+
    "\n*/price BTC UAH* — _краткая цена в валюте которую вы указали второй_"+ 
    "\n*/price 24h% BTC* — _изменения в цене за 24 часа в процентах (Имеется 3 аргумента: 24h%, 7d%, 30d%)_"+
    "\n*/price 24h BTC* — _изменения в цене за 24 часа (Можно указать вторую валюту: /price 24h BTC UAH. В таком случае изменения в цене будут показываться во второй валюте которую вы указали)_"+ 
    "\n\nℹ️_В параметрах выше BTC и UAH были указаны для примера. Можно использовать любые валюты (Кроме команд /btc и /pbtc, это специальный команды для быстрого мониторинга цены BTC)_")