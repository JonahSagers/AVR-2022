import time
import math

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")

if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()
    placeholder = 0
    while True:
        placeholder += 0.1
        saturation = 50 + (math.sin(placeholder) * 50)
        box.send_message("avr/pcm/set_base_color", {"wrgb": [0, 0, int(saturation), 0]})
        logger.debug(saturation)
        time.sleep(0.025)