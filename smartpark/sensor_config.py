import config_parser

CONFIG_FILE = 'config.toml'


class SensorConfig(config_parser.MqttDeviceConfig):
    def __init__(self):
        super().__init__()

    def write_config_to_toml(self):
        config_file = open(CONFIG_FILE, 'w')

        config_file.write(f'[[Sensors]]\n'
                          f'name = "{self.name}"\n'
                          f'location = "{self.location}"\n'
                          f'topic-root = "{self.topic_root}"\n'
                          f'topic-qualifier = "{self.topic_qualifier}"\n'
                          f'broker = "{self.broker}"\n'
                          f'port = "{self.port}"\n\n')
