from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


BTN_WEATHER = InlineKeyboardButton('🌦️ Weather', callback_data="weather")
BTN_ADDITIONAL_INFO = InlineKeyboardButton('📄 More info', callback_data="additional_info")
BTN_SHARE_GEO = KeyboardButton("📍 Share with GEO", request_location=True)

START = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(BTN_SHARE_GEO)
HELP = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_ADDITIONAL_INFO)
WEATHER = InlineKeyboardMarkup().add(BTN_ADDITIONAL_INFO)
ADDITIONAL_INFO = InlineKeyboardMarkup().add(BTN_WEATHER)
