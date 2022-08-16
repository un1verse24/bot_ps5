from aiogram import types, Bot, Dispatcher, executor
from config import BOT_TOKEN
from keyboards import kb
from bot_ps5_parcer.all_shops_parcer import AllShopsScraper

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)

async def on_startup(_):
    print('I am ready')


@dp.message_handler(commands='start')
async def start_command(messsage: types.Message):
    await messsage.answer('Список команд', reply_markup=kb)

@dp.message_handler(commands='search')
async def get_ps5_info(message: types.Message):
    scraper = AllShopsScraper()
    lst = scraper.get_data()
    for item in lst:
        await bot.send_message(chat_id=message.from_user.id, text=f"{item['name']} - {item['price']} - {item['link']}")






if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
