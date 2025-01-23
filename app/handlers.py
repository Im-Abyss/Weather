from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import requests  # Импортируем requests для выполнения HTTP-запросов

from config import API_key
from .FSM import Weather

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer_photo(photo='AgACAgIAAxkBAAMCZ5ETn-c6RiYq7kYAAfM2kbIxwr_6AAKO6jEb41GJSGS41lDGLBTQAQADAgADeQADNgQ',
                               caption='Здравствуйте! ✋\nКакой город будем смотреть? 😊')
    await state.set_state(Weather.city)

@router.message(Weather.city)
async def weather(message: Message, state: FSMContext):
    city_name = message.text
    response_k = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    try:
        response = requests.get(response_k)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            await message.answer(f'Погода в городе {city_name} сейчас {temperature}°C')
        else:
            await message.answer(f'Не удалось получить данные о погоде для города {city_name}. Попробуйте другой город.')
    except Exception as e:
        await message.answer('Произошла ошибка при запросе данных о погоде. Пожалуйста, попробуйте позже.')

    await state.clear()