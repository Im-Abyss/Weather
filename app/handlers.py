from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import requests

from config import API_key
from .FSM import Weather
from .keyboards import change_city

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer_photo(photo='AgACAgIAAxkBAAMCZ5ETn-c6RiYq7kYAAfM2kbIxwr_6AAKO6jEb41GJSGS41lDGLBTQAQADAgADeQADNgQ',
                               caption='Здравствуйте! ✋\nКакой город будем смотреть? 😊')
    await state.set_state(Weather.city)

@router.callback_query(F.data == 'change_city')
async def new_city(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Другой город')
    await callback.message.edit_text('Укажите другой город, пожалуйста 🤔')
    await state.set_state(Weather.city)

@router.message(Weather.city)
async def weather(message: Message, state: FSMContext):
    city_name = message.text
    response_k = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru'
    try:
        response = requests.get(response_k)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            await message.answer(f'Погода в городе {city_name} сейчас {temperature}°C, {weather_description}.', reply_markup=change_city)
        else:
            await message.answer(f'Не удалось получить данные о погоде для города {city_name}. Попробуйте другой город.')
    except Exception as e:
        await message.answer('Произошла ошибка при запросе данных о погоде. Пожалуйста, попробуйте позже.')
        await new_city(message, state)
    
    await state.clear()