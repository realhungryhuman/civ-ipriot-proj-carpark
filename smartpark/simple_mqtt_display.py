import mqtt_device
import time
import tomli
from config_parser import parse_config
from sys import argv

DEVICE_NUMBER = int(argv[1]) - 1


class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('lot/moondalup/display1/na')
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
       # Already done(?)


if __name__ == '__main__':
    # TODO: Read config from file
    config = parse_config()
    display = Display(config['Displays'][DEVICE_NUMBER])
    print(f"{display.name} initialized")
