from mistralai import Mistral

from config import AI_TOKEN


async def main(content):

    '''
    Эта функция, которая позволяет боту
    давать рекомендации к погоде
    '''

    api_key = AI_TOKEN
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    response = await client.chat.complete_async(
        model=model,
        messages=[
             {
                  "role": "user",
                  "content": f"Напиши вот эту погоду и дай рекомендацию или пожелания к ней: {content}. То есть, например, 'Погода в городе Москва сейчас -3.53°C, пасмурно. Я рекомендую вам [то, что ты рекомендуешь], и желаю [то, что ты желаешь]. Там где я поставил квадратные скобки, тебе их ставить не надо. И ещё, добавь смайлики пожалуйста для настроения",
              },
        ],
    )
    
    return response.choices[0].message.content