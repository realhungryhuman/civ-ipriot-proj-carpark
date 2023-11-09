from datetime import datetime

import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage

import tomli

from config_parser import parse_config
from sys import argv

CONFIG_FILE = "config.toml"
DEVICE_NUMBER = int(argv[1]) - 1


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()
        self._temperature = None

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + f"TEMPC: {self._temperature}"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + f"TEMPC: {self._temperature}"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        # TODO: Extract temperature from payload
        self._temperature = payload.split(", ")[1]
        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    # TODO: Read config from file
    config = parse_config()
    car_park = CarPark(config['CarParks'][DEVICE_NUMBER])
    print(f"Carpark {car_park.name} initialized")
