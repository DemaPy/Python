from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from requestsToBinance import download_stepn, download_fantasy, download_zombie
import json
import time


bot = Bot(token='5358113262:AAGSqhT9l3rEamqkZpEFZw0Rt8Hst_sw_yI', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_button = ['👟STEPN x ASICS NFT Sneakers', '😵Zombie NFTs by Braindom Games', '✨TAP FANTASY METAVERSE']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)


    await message.answer('🎲Выбери категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='👟STEPN x ASICS NFT Sneakers'))
async def start(message: types.Message):
    await message.answer('Подожди... кросы подтягиваются')

    download_stepn()
    with open('stepn.json') as file:
        nfts = json.load(file)

    for items in nfts['data']['rows']:
        card = hlink(items["title"], "https://www.binance.com/ru/nft/goods/detail?productId={0}&isProduct=1").format(items["productId"])

        await message.answer(card)
        
        # if items['amount'] <= "4":
        #     print(items)




@dp.message_handler(Text(equals='😵Zombie NFTs by Braindom Games'))
async def start(message: types.Message):
    await message.answer('Подожди... загружаю зомби коллекцию')

    download_zombie()
    with open('zombie.json') as file:
        nfts = json.load(file)

    for items in nfts['data']['rows']:
        card = hlink(items["title"], "https://www.binance.com/ru/nft/goods/detail?productId={0}&isProduct=1").format(items["productId"])

        await message.answer(card)




@dp.message_handler(Text(equals='✨TAP FANTASY METAVERSE'))
async def start(message: types.Message):
    await message.answer('Подожди... ню коллекция уже на подходе')

    download_fantasy()
    with open('fantasy.json') as file:
        nfts = json.load(file)

    for items in nfts['data']['rows']:
        card = hlink(items["title"], "https://www.binance.com/ru/nft/goods/detail?productId={0}&isProduct=1").format(items["productId"])

        await message.answer(card)



def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
