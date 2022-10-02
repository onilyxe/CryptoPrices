from plugins import new_message, restricted
import yaml


@restricted.restricted
def plugin(update, context):
    new_message.new_message(update)

    if not context.args:
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown',
            text='⚙️*Plugins*\n`/plugin list` — _список плагинов._\n`/plugin enable [name]` — _включить плагин._\n`/plugin disable [name]` — _выключить плагин._')
        return

    def switch_state(args, desired_state):
        if not args[1]:
            context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown',
                text='⚙️Plugins\n*/plugin list* — список плагинов.\n*/plugin enable [name]* — включить плагин.\n*/plugin disable [name]* — выключить плагин.')
        if context.args[1] in config['PLUGINS']:
            if config['PLUGINS'][args[1]] != desired_state:
                config['PLUGINS'][args[1]] = desired_state
                context.bot.send_message(chat_id=update.message.chat_id, text=f'🚀Успешно!')
            else:
                context.bot.send_message(chat_id=update.message.chat_id, text=f'ℹ️Не думаю что смогу сделать это дважды')
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text=f'ℹ️Невозможно найти "{args[1]}"')

    # load config.yaml
    with open('config.yaml', 'r+') as f:
        config = yaml.full_load(f)

        if context.args[0] == 'list':
            plugin_list = ['✅    ' + plugins + '\n' if config['PLUGINS'][plugins] else '❌    ' + plugins + '\n' for plugins in config['PLUGINS']]
            context.bot.send_message(chat_id=update.message.chat_id, text=''.join(plugin_list))
        if context.args[0] == 'enable':
            switch_state(context.args, True)
        if context.args[0] == 'disable':
            switch_state(context.args, False)
        f.seek(0)
        yaml.dump(config, f)