"""A class or function to parse the config file and return the values as a dictionary.

The config file itself can be any of the following formats:

- ryo: means 'roll your own' and is a simple text file with key-value pairs separated by an equals sign. For example:
```
location = "Moondalup City Square Parking"
number_of_spaces = 192
```
**you** read the file and parse it into a dictionary.
- json: a json file with key-value pairs. For example:
```json
{location: "Moondalup City Square Parking", number_of_spaces: 192}
```
json is built in to python, so you can use the json module to parse it into a dictionary.
- toml: a toml file with key-value pairs. For example:
```toml
[location]
name = "Moondalup City Square Parking"
spaces = 192
```
toml is part of the standard library in python 3.11, otherwise you need to install tomli to parse it into a dictionary.
```bash
python -m pip install tomli
```
see [realpython.com](https://realpython.com/python-toml/) for more info.

Finally, you can use `yaml` if you prefer.



"""
import tomli

CONFIG_FILE = 'config.toml'


class MqttDeviceConfig:
    def __init__(self):
        self.config = parse_config()
        self.name = self.config['name']
        self.location = self.config['location']
        self.topic_root = self.config['topic-root']
        self.topic_qualifier = self.config['topic-qualifier']
        self.broker = self.config['broker']
        self.port = self.config['port']

    def write_config_to_toml(self):
        config_file = open(CONFIG_FILE, 'w')

        config_file.write(f'[[MqttDevices]]\n'
                          f'name = "{self.name}"\n'
                          f'location = "{self.location}"\n'
                          f'topic-root = "{self.topic_root}"\n'
                          f'topic-qualifier = "{self.topic_qualifier}"\n'
                          f'broker = "{self.broker}"\n'
                          f'port = "{self.port}"\n\n')


def parse_config() -> dict:
    """Parse the config file and return the values as a dictionary"""
    # TODO: get the configuration from a parsed file
    with open(CONFIG_FILE, "r") as file:
        config_string = file.read()
    config = tomli.loads(config_string)

    return config
