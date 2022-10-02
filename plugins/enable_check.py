import yaml


# Check if a plugin is enabled before allowing it to run
def enable_check(plugin):
    with open('config.yaml', 'r') as f:
        config = yaml.full_load(f)
        # Remove first 8 character from plugin name ("plugins.")
        return not config['PLUGINS'][plugin[8:]]