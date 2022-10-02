import os
import yaml


if os.path.isfile('./config.yaml'):
    dir_list = os.listdir('plugins')
    plugin_list = []
    with open('config.yaml', 'r+') as f:
        config = yaml.full_load(f)

        try:
            if not config['PLUGINS']:
                config['PLUGINS'] = []
        except KeyError:
            config['PLUGINS'] = {}

        for file_name in dir_list:
            if file_name[0] != '_':
                plugin_list.append(file_name[:-3])
                system_plugins = ['new_message', 'restricted', 'plugin', 'enable_check']
                if file_name[:-3] not in config['PLUGINS'] and file_name[:-3] not in system_plugins:
                    config['PLUGINS'][file_name[:-3]] = True
        f.seek(0)
        yaml.dump(config, f)
    plugins = '\n'.join(plugin_list)
    print(f'Plugins ({len(plugin_list)}): \n{plugins}')

    __all__ = plugin_list
else:
    print('No config.yaml file found, make sure to add your info to config.yaml.example and rename it to config.yaml')
    quit()