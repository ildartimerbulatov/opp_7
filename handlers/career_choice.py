from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keyboards.prof_keyboards import make_row_keyboard


router = Router()


available_jobs = [
    "Программист ",
    "Дизайнер",
    "Маркетолог",
    ]

available_grades = ['Junior', 'Middle', 'Senior']

class ChoiceProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer(
        "Выберете профессию",
        reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoiceProfile.job)

@router.message(ChoiceProfile.job,F.text.in_(available_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        "Выберете уровень",
        reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoiceProfile.grade)


@router.message(ChoiceProfile.job)
async def prof_chosen_incorrect(message: types.Message, state: FSMContext):
    await message.answer(
        "Выберете уровень",
        reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoiceProfile.grade)


@router.message(ChoiceProfile.grade,F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = state.get_data()
    await message.answer(f"Ваша профессия: {user_data['profession']}\n"
                         f"Ваш уровень: {message.text}",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(ChoiceProfile.grade)
async def grade_chosen_incorrect(message: types.Message):
    await message.answer(
        text="Выберете уровень",
        reply_markup=make_row_keyboard(available_grades))
