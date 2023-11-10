import mqtt_device
import time
import tomli

CONFIG_FILE = "config.toml"

class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message()
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
       data = msg.payload.decode()
       self.display(*data.split(','))
       # TODO: Parse the message and extract free spaces,\
       #  temperature, time


if __name__ == '__main__':
    # TODO: Read config from file
    displays = []
    with open(CONFIG_FILE, "r") as file:
        config_string = file.read()
    loaded_config = tomli.loads(config_string)
    config = loaded_config['Displays']
    for display in config:
        displays.append(Display(display))
        print(f"{displays[display].name} initialized")
    # with open(CONFIG_FILE, "r") as file:
    #     config_string = file.read()
    # config = tomli.loads(config_string)
    # config = config["CarParks"][0]
    # config["name"] = config["Display"][0]["name"]
    # config = {'name': 'display',
    #  'location': 'L306',
    #  'topic-root': "lot",
    #  'broker': 'localhost',
    #  'port': 1883,
    #  'topic-qualifier': 'na'
    #  }

