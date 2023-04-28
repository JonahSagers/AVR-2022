import time

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")

    def hello_world(self) -> None:
        logger.debug("Hello world")

        payload = AvrPcmSetBaseColorPayload(wrgb=(0, 0, 255, 0))
        box.send_message("avr/pcm/set_base_color", payload)

        logger.debug("Light changed")


if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()
    payload = AvrPcmSetBaseColorPayload(wrgb=(0, 0, 255, 0))
    box.send_message("avr/pcm/set_base_color", payload)
    #box.hello_world()

    while True:
        time.sleep(0.1)