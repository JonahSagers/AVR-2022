import time
import math

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")

    def hello_world(self) -> None:
        logger.debug("Hello world")
        placeholder = 0
        while True:
            placeholder += 1
            payload = AvrPcmSetBaseColorPayload(wrgb=((1 + math.sin(placeholder)) * 127.5, (1 + math.sin(placeholder)) * 127.5, 0, 0))
            box.send_message("avr/pcm/set_base_color", payload)

        logger.debug("Light changed")


if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()

    box.hello_world()

    while True:
        time.sleep(0.1)