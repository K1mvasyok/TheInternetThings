from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📖 Погода"), KeyboardButton(text="📚 Погода")],
            [KeyboardButton(text="🎓 Погода"), KeyboardButton(text="📅 Погода")],], 
        resize_keyboard=True, input_field_placeholder="Выберите пункт ниже")