from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='stop')
button3 = types.KeyboardButton(text="Узнать больше о клиниках \"ЗдравКлиник\"")
button4 = types.KeyboardButton(text="Ознакомиться с условиями Программы лояльности")
button5 = types.KeyboardButton(text="Срочно записаться на прием в клинику")
button6 = types.KeyboardButton(text='/prof')
button7 = types.KeyboardButton(text="Пройти идентификацию")
button8 = types.KeyboardButton(text="Иванов Сергей Александрович")
button9 = types.KeyboardButton(text="Петрова Анна Викторовна")
button10 = types.KeyboardButton(text="Смирнов Дмитрий Николаевич")
button11 = types.KeyboardButton(text="Кузнецова Елена Андреевна")
button12 = types.KeyboardButton(text="Сидоров Алексей Павлович")

keyboard1 = [
    [button3, button4, button5],
    [button2],
]

keyboard2 = [
    [button8, button9, button12],
    [button10, button11, button2],
]

keyboard3 = [
    [button7],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
kb3 = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)
