from mistralai import Mistral

from config import AI_TOKEN, PROMT


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
                  "content": PROMT,
              },
        ],
    )
    
    return response.choices[0].message.content