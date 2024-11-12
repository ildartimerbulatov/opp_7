from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    #for button in buttons:
    #    row.append(KeyboardButton(text=button))
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    #return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    #return ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)