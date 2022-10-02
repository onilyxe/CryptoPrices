from telegram.ext import Updater, CommandHandler
import yaml
import logging
from plugins import *


def start_bot():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger('apscheduler.executors.default').propagate = False

    with open('config.yaml', 'r') as f:
        config = yaml.full_load(f)

    api_key = config['TELEGRAM']['API_KEY']

    updater = Updater(token=api_key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start.start))
    dispatcher.add_handler(CommandHandler('help', help.help))
    dispatcher.add_handler(CommandHandler('btc', btc.btc))
    dispatcher.add_handler(CommandHandler('pbtc', pbtc.pbtc))
    dispatcher.add_handler(CommandHandler('p', p.p))
    dispatcher.add_handler(CommandHandler('price', price.price))
    dispatcher.add_handler(CommandHandler('plugin', plugin.plugin))

    updater.start_polling(drop_pending_updates=True)
    updater.idle()

if __name__ == '__main__':
    start_bot()