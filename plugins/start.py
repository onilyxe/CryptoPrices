import plugins


def start(update, context):
    plugins.new_message.new_message(update)

    if plugins.enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "👋Привет. Я умею показывать текущую цену криптовалют.\n✍️Напиши */help* чтобы узнать как мной пользоваться.")