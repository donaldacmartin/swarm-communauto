"""swarm_communauto.communauto

This module contains any interaction with the Communauto API

Functions:
    get_vehicles() -> List[Vehicle]
"""

from logging import error
from typing import List

from requests import RequestException, get

from .model import Vehicle


BASE_URL = "https://www.reservauto.net"
PATH = "/WCF/LSI/LSIBookingServiceV3.svc/GetAvailableVehicles"
PARAMETERS = {"BranchID": 1, "LanguageID": 0}


def get_vehicles() -> List[Vehicle]:
    """Get all available vehicles"""

    try:
        with get(f"{BASE_URL}{PATH}", params=PARAMETERS) as response:
            vehicles = response.json()["d"]["Vehicles"]

            return [
                Vehicle(
                    brand=vehicle["CarBrand"],
                    model=vehicle["CarModel"],
                    colour=vehicle["CarColor"],
                    plate=vehicle["CarPlate"],
                    position=(vehicle["Latitude"], vehicle["Longitude"]),
                    distance=None,
                )
                for vehicle in vehicles
            ]
    except RequestException as request_error:
        error(f"Error contacting the API: {request_error}")
    except (TypeError, ValueError) as parse_error:
        error(f"Error parsing response: {parse_error}")

    return []
