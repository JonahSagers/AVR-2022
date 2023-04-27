import time

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrFcmVelocityPayload, AvrPcmSetBaseColorPayload
from loguru import logger


class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")
        self.topic_map = {"avr/fcm/velocity": self.show_velocity}

    def show_velocity(self) -> None:
        payload = AvrFcmVelocityPayload
        vx = payload["vX"]
        vy = payload["vY"]
        vz = payload["vZ"]
        v_ms = (vx, vy, vz)
        print(f"Velocity information: {v_ms} m/s")

    def hello_world(self) -> None:
        logger.debug("Hello world")

        payload = AvrPcmSetBaseColorPayload(wrgb=(0, 100, 0, 0))
        self.send_message("avr/pcm/set_base_color", payload)

        logger.debug("Light changed")


if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()
    box.show_velocity()
    box.hello_world()

    while True:
        time.sleep(0.1)