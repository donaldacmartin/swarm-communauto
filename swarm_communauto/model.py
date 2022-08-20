"""swarm_communauto.model

This module contains the model classes for the swarm_communauto application.

Classes:
    GeoPosition: A class that represents a geographic position.
    MQTTConfig: A class that represents the configuration for MQTT.
    Vehicle: A class that represents a vehicle.
"""

from dataclasses import dataclass
from typing import Optional, Tuple


GeoPosition = Tuple[float, float]


@dataclass
class MQTTConfig:
    """MQTT configuration"""

    host: str
    port: int
    topic: str
    client_id: str


@dataclass
class Vehicle:
    """A Communauto vehicle"""

    brand: str
    model: str
    colour: str
    plate: str
    position: GeoPosition
    distance: Optional[float]
