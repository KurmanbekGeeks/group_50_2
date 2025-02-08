# FSM_registration.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_reg(StatesGroup):
    fullname = State()
    age = State()
    male = State()
    date_age = State()
    email = State()
    photo = State()


async def start_fsm_reg(message: types.Message):
    await FSM_reg.fullname.set()
    await message.answer('Введите своё фио: ')


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await FSM_reg.next()
    await message.answer('Отправь свой возраст')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await state.finish()

    await message.answer(f'Ваши данные\n'
                         f'ФИО - {data["fullname"]}\n'
                         f'Возраст - {data["age"]}\n')




def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['registration'])
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_age, state=FSM_reg.age)