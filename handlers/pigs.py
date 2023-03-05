import os
from random import choice
from aiogram import types

GIF_DIR = os.path.dirname(__file__).replace('handlers', 'gif')
print(GIF_DIR)


async def get_random_gif(message: types.Message):
    random_gif = choice(os.listdir(GIF_DIR))
    with open(os.path.join(GIF_DIR, random_gif), 'rb') as gif:
        await message.reply_animation(gif, caption='This is your random gif \U0001F916')
