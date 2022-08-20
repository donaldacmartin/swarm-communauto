"""swarm_ecowitt.mqtt
This module contains the MQTT client.
Functions:
    publish_message(str, str, int, str, dict) -> None
"""

from dataclasses import asdict
from json import dumps
from logging import info, error
from typing import List

from paho.mqtt import MQTTException
from paho.mqtt.publish import single

from .model import MQTTConfig, Vehicle


def publish_vehicles(vehicles: List[Vehicle], config: MQTTConfig) -> None:
    """Publish a message to the MQTT broker."""

    try:
        info("Publishing payload to MQTT")

        single(
            topic=config.topic,
            payload=dumps([asdict(vehicle) for vehicle in vehicles]),
            hostname=config.host,
            port=config.port,
            client_id=config.client_id,
        )

        info("Message published")
    except ValueError as value_error:
        error(f"Failed to serialise payload: {value_error}")
    except MQTTException as mqtt_exception:
        error(f"Failed to publish message: {mqtt_exception}")
