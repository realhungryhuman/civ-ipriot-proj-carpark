import config_parser

CONFIG_FILE = 'config.toml'


class CarparkConfig(config_parser.MqttDeviceConfig):
    def __init__(self):
        super().__init__()
        self.total_spaces = self.config['total-spaces']
        self.total_cars = self.config['total-cars']
        self.free_spaces = None

    def write_config_to_toml(self):
        config_file = open(CONFIG_FILE, 'w')

        config_file.write(f'[[CarParks]]\n'
                          f'name = "{self.name}"\n'
                          f'total-spaces = "{self.total_spaces}"\n'
                          f'total-cars = "{self.total_cars}"\n'
                          f'location = "{self.location}"\n'
                          f'topic-root = "{self.topic_root}"\n'
                          f'broker = "{self.broker}"\n'
                          f'port = "{self.port}"\n'
                          f'topic-qualifier = "{self.topic_qualifier}"\n\n')
