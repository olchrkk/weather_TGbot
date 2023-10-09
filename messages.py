from coordinates import get_coordinates
from services.api import get_weather


def weather(coordinates) -> str:
    data = get_weather(coordinates)
    return f"📍 {data.location}.\n" \
           f"🌡️ Temperature is {data.temperature}, but feels like {data.temperature_feeling}.\n" \
           f"📄 {data.description}."


def additional_info(coordinates) -> str:
    data = get_weather(coordinates)
    return f"💨 Wind speed is {data.wind_speed}.\n" \
           f"🧭 Directed to {data.wind_direction}.\n" \
           f"🌡️ Pressure is {data.pressure}.\n" \
           f"🌫️ Humidity is {data.humidity}." 

def help() -> str:
    return "Hello! Please, use one of theese buttons below:"
