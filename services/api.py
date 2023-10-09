from enum import IntEnum
from dataclasses import dataclass
from services.config import CURRENT_WEATHER_GET
import requests
import json
from coordinates import Coordinates

@dataclass(frozen=True)
class Weather:
    location: str
    description: str
    wind_speed: float
    wind_direction: str
    temperature: str
    temperature_feeling: str
    pressure: str
    humidity: str


class WindDirection(IntEnum):
    North = 0
    NorthEast = 45
    East = 90
    SouthEast = 135
    South = 180
    SouthWest = 225
    West = 270
    NorthWest = 315


def _get_weather_response(latitude: float, longitude: float) -> dict:
    url = CURRENT_WEATHER_GET.format(lat=latitude, lon=longitude)
    data = requests.get(url)
    return json.loads(data.text)


def get_weather(coordinates: Coordinates) -> Weather:
    data = _get_weather_response(coordinates.latitude, coordinates.longitude)
    return Weather(
        location=_parse_location(data),
        description=data["weather"][0]["description"].capitalize(),
        wind_speed= f'{data["wind"]["speed"]} M/S',
        wind_direction=_parse_wind_direction(data),
        temperature=f'{data["main"]["temp"]} °С',
        temperature_feeling=f'{data["main"]["feels_like"]} °C',
        pressure=f'{data["main"]["pressure"]} Pa',
        humidity=f'{data["main"]["humidity"]} %'
    )


def _parse_location(data: dict) -> str:
    city = data["name"]
    country_code = data["sys"]["country"]
    return f"{city}, {country_code}"


def _parse_wind_direction(data: dict) -> str:
    direction_degrees = round(data['wind']['deg'] / 45) * 45
    return WindDirection(direction_degrees).name
