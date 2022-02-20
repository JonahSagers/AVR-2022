import copy
import json
from typing import Any, Dict, Protocol, Union

import paho.mqtt.client as mqtt
from loguru import logger


class MQTTCallable(Protocol):
    def __call__(self, payload: Any) -> Any:
        ...


class MQTTModule:
    """
    Generic MQTT Module class that should be inherited by other modules.
    `topic_prefix` should be a lowercase string that is the namespace
    for the class's MQTT messages. Additionally, the `topic_map` should
    be a dictionary of topics to functions that will be called with a dictionary
    payload.
    """

    def __init__(self):
        # these should be not be changed, to match the docker-compose.yml file
        self.mqtt_host = "mqtt"
        self.mqtt_port = 18830

        # create the MQTT client
        self.mqtt_client = mqtt.Client()

        # set up the on connect and on message handlers
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

        # dictionary of MQTT topics to callback functions
        # this is intended to be overwritten by the child class
        self.topic_map: Dict[str, MQTTCallable] = {}

        # maintain a cache of the last message sent on a topic by this module
        self.message_cache: Dict[str, dict] = {}

    def run(self) -> None:
        """
        Class entrypoint. Connects to the MQTT broker and starts the MQTT loop.
        """
        # connect the MQTT client
        self.mqtt_client.connect(host=self.mqtt_host, port=self.mqtt_port, keepalive=60)
        # run forever
        self.mqtt_client.loop_forever()

    def on_message(
        self, client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage
    ) -> None:
        """
        On message callback, Dispatches the message to the appropriate function.
        """
        try:
            logger.debug(f"Recieved {msg.topic}: {msg.payload}")
            if msg.topic in self.topic_map:
                # we talk JSON, no exceptions
                payload = json.loads(msg.payload)
                self.topic_map[msg.topic](payload)

        except Exception as e:
            logger.exception(f"Error handling message on {msg.topic}")

    def on_connect(
        self,
        client: mqtt.Client,
        userdata: Any,
        rc: Any,
        properties: mqtt.Properties = None,
    ) -> None:
        """
        On connection callback. Subscribes to MQTT topics in the topic map.
        """
        logger.debug(f"Connected with result code {rc}")

        for topic in self.topic_map.keys():
            client.subscribe(topic)
            logger.success(f"Subscribed to: {topic}")

    def send_message(self, topic: str, payload: Any) -> None:
        """
        Sends a message to the MQTT broker.
        """
        logger.debug(f"Sending message to {topic}: {payload}")
        self.mqtt_client.publish(topic, json.dumps(payload))
        self.message_cache[topic] = copy.deepcopy(payload)