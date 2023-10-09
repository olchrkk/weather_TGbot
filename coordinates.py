from dataclasses import dataclass
import json
import requests


@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    data = requests.get(url)
    return json.loads(data.text)


def get_coordinates() -> Coordinates:
    data = _get_ip_data()
    lat, long = data['loc'].split(',') 
    return Coordinates(lat, long)
