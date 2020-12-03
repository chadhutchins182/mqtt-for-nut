import paho.mqtt.client as mqttClient
import logging
from typing import Any, Dict
import os
import time
from . import mqttConfig
log = logging.getLogger("mqtt-for-nut")


config = mqttConfig.mqttConfig()
client = mqttClient.Client()


def _connect_mqtt(self) -> None:

    mqtt_host = config.get_mqtt_host()
    mqtt_port = config.get_mqtt_port()
    log.info(f"Connecting to MQTT broker {mqtt_host}:{mqtt_port}...")
    client.connect(host=config.mq, port=mqtt_port, keepalive=60)
    client.loop_start()
    while not client.is_connected():
        time.sleep(10)
        log.debug("Connecting to broker...")
    log.info(f"MQTT Broker connected: {client.is_connected()}")


def is_connected() -> bool:
    """[summary]

    Returns:
        bool: [description]
    """
    return client.is_connected()


def sendSingle(msg):
    """[summary]

    Args:
        msg ([type]): [description]
    """

    if is_connected():
        log.info("Sent Message to Topic ", config.get_mqtt_base_topic)
        client.publish(config.get_mqtt_topic(), payload=msg)
    else:
        log.error("No Client Connected")


def setupClient():

    base_topic = os.environ.get('base_topic', 'home/ups')
    if not base_topic.endswith('/'):
        base_topic += '/'

    # Read env vars passed in by Docker run
    mqtt_config = {
        'ups_host': os.environ.get('ups_hostname', 'localhost'),
        'mqtt_host': os.environ.get('mqtt_hostname', 'localhost'),
        'mqtt_port': int(os.environ.get('mqtt_port', 1883)),
        'mqtt_user': os.environ.get('mqtt_username', None),
        'mqtt_password': os.environ.get('mqtt_password', None),
        'interval': int(os.environ.get('interval', 60))
    }

    config = mqttConfig.mqttConfig(**mqtt_config)

    _connect_mqtt()


if __name__ == "__main__":
    setupClient()
