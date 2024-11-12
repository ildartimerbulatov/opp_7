from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.randomfox import fox
from less3.keyboards.keyboards import kb1, kb2, kb3

from random import randint

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    text = "Вас приветствует чат-бот Программы лояльности сети клиник неврологии и ортопедии \"ЗдравКлиник\" 👋\n"
    text += "Я - Ваш персональный помощник!\n"
    text += "Для начала мне нужно идентифицировать Вас в качестве пациента нашей клиники.\n"
    text += "1️⃣ Нажмите кнопку Пройти идентификацию, которая расположена ниже ⬇️\n"
    await message.answer(f'Привет, {name}')
    await message.answer(text)
    await message.answer("Нажмите на кнопку ниже", reply_markup=kb3)

@router.message(F.text == "Пройти идентификацию")
async def identificator(message: types.Message):
    await message.answer(f"Ваш ID: {message.chat.id}")
    await message.answer(f"Ваш username: {message.chat.username}")
    await message.answer(f"Ваше имя: {message.chat.first_name}")
    await message.answer(f"Ваша фамилия: {message.chat.last_name}")
    if hasattr(message.chat, 'language_code'):
        await message.answer(f"Ваш язык: {message.chat.language_code}")
    else:
        await message.answer("Ваш язык не указан")
    await message.answer("Идентификация пройдена")
    await message.answer("Выберите, что Вы хотите сделать ⬇", reply_markup=kb1)

@router.message(F.text == "Узнать больше о клиниках \"ЗдравКлиник\"")
async def about_clinics(message: types.Message):
    text = (
        "Сеть клиник неврологии и ортопедии «ЗдравКлиник» уже более 15 лет предоставляет высококачественные медицинские услуги. "
        "Мы гордимся тем, что помогли множеству людей восстановить здоровье! 💪\n\n"
        "В наших клиниках работают высококвалифицированные врачи, которые постоянно совершенствуют свои навыки и следят за современными тенденциями в медицине. 🩺\n\n"
        "Мы заботимся о вашем здоровье и предлагаем доступные цены, льготы, скидки и возможность оплаты в рассрочку. 💰 "
        "Каждую неделю проводим бесплатные лекции о здоровье и современных методах лечения.\n\n"
        "Ваше здоровье — наша приоритетная задача! 🌟"
    )
    await message.answer(text)

@router.message(F.text == "Ознакомиться с условиями Программы лояльности")
async def loyalty_program(message: types.Message):
    text = (
        "Условия лояльности в сети клиник «ЗдравКлиник»\n\n"
        "Мы ценим наших клиентов и стремимся делать медицинские услуги доступнее! 🌟 В рамках программы лояльности мы предлагаем ряд преимуществ для наших постоянных пациентов:\n\n"
        "1. Скидки на услуги: При повторном обращении вы можете рассчитывать на скидку до 20% на определенные процедуры и консультации. 💸\n\n"
        "2. Бонусная программа: Накапливайте бонусы за каждое посещение и используйте их для оплаты последующих услуг. Бонусы можно также передавать друзьям и близким! 🎁\n\n"
        "3. Специальные предложения: Участие в акциях и распродажах, которые проводятся регулярно, позволит вам получать дополнительные скидки и подарки. 📅\n\n"
        "4. Приоритетное обслуживание: Наши постоянные клиенты имеют право на приоритетное запись на прием к специалистам, что экономит ваше время. ⏳\n\n"
        "5. Бесплатные консультации: Участие в программе лояльности дает возможность получить бесплатные консультации по актуальным вопросам здоровья и профилактики заболеваний. 🗣️\n\n"
        "6. Подарочные сертификаты: Мы предлагаем возможность приобретения подарочных сертификатов на услуги клиники, которые могут стать отличным подарком для ваших близких. 🎉\n\n"
        "Ваше здоровье и комфорт — наша главная задача! Присоединяйтесь к программе лояльности «ЗдравКлиник» и получайте больше преимуществ от вашего обращения к нам! ❤️"
    )
    await message.answer(text)

@router.message(F.text == "Срочно записаться на прием в клинику")
async def urgent_appointment(message: types.Message):
    await message.answer("Пожалуйста, выберите специалиста для записи на прием:", reply_markup=kb2)

@router.message(F.text == "stop")
async def stop_action(message: types.Message):
    await message.answer("Вы вернулись к предыдущему выбору. Пожалуйста, выберите, что вы хотите сделать ⬇", reply_markup=kb1)

@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)

@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    numbers = randint(1, 10)
    await message.answer(f"{numbers}")

@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if msg_user == "пройти идентификацию":
        return
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока, {name}')
    elif 'ты кто' == msg_user:
        await message.answer(f'Я эхобот на aiogram 3, {name}')
    elif 'лиса' in msg_user:
        await message.answer(f'выбери клавишу покажи лису, {name}', reply_markup=kb2)
    elif 'ура' in msg_user:
        await message.answer("УРААА")
    elif msg_user == "инфо":
        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(f'Я не знаю такого слова')
