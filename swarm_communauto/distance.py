"""swarm_communauto.distance

This module contains distance calculations.

Functions:
    add_distance(Vehicle, GeoPosition) -> Vehicle
"""

from geopy import distance
from swarm_communauto.model import GeoPosition, Vehicle


def add_distance(vehicle: Vehicle, home: GeoPosition) -> Vehicle:
    """Add the distance to the vehicle from the home position"""

    vehicle.distance = distance.distance(home, vehicle.position).km
    return vehicle
