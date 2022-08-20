"""swarm_communauto.__main__

This module is the entry point for the application.

Functions:
    main() -> None
"""

from logging import INFO, basicConfig, info

from .local_config import get_config
from .distance import add_distance
from .communauto import get_vehicles
from .mqtt import publish_vehicles


def main() -> None:
    """Main entry point for the application"""

    info("Getting config")
    home, cut_off, mqtt_config = get_config()

    info("Getting vehicles")
    vehicles = [add_distance(vehicle, home) for vehicle in get_vehicles()]
    sorted_vehicles = sorted(vehicles, key=lambda vehicle: vehicle.distance)

    vehicles_in_range = [
        vehicle for vehicle in sorted_vehicles if vehicle.distance < cut_off
    ]

    info(f"Found {len(vehicles_in_range)} vehicle(s) under {cut_off}km")
    publish_vehicles(vehicles_in_range, mqtt_config)


if __name__ == "__main__":
    basicConfig(level=INFO, format="%(asctime)s %(levelname)s %(message)s")
    main()
