"""swarm_communauto.local_config

This module is used to get the config from environment variables.

Functions:
    get_config() -> Union[GeoPosition, float, MQTTConfig]
"""

from logging import error
from os import environ
from typing import Union

from .model import GeoPosition, MQTTConfig


def _get_home_from_env() -> GeoPosition:
    return (float(environ["HOME_LAT"]), float(environ["HOME_LON"]))


def _get_cutoff_from_env() -> float:
    return float(environ["CUTOFF"])


def _get_mqtt_config_from_env() -> MQTTConfig:
    return MQTTConfig(
        host=environ["MQTT_HOST"],
        port=int(environ["MQTT_PORT"]),
        topic=environ["MQTT_TOPIC"],
        client_id=environ["MQTT_CLIENT_ID"],
    )


def get_config() -> Union[GeoPosition, float, MQTTConfig]:
    """Get the configuration for the application"""

    try:
        return _get_home_from_env(), _get_cutoff_from_env(), _get_mqtt_config_from_env()
    except KeyError as key_error:
        error(f"Failed to get config: {key_error}")
        raise ValueError(f"Missing environment variable: {key_error}") from key_error
