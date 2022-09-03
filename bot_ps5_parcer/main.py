import time
from aiogram import types, Bot, Dispatcher, executor
from config import BOT_TOKEN
from keyboards import kb
from bot_ps5_parcer.all_shops_parcer import AllShopsScraper
from bot_ps5_parcer.store_scrapers.Mediaexpert import MediaExpertScraper


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

@dp.message_handler(commands='smart')
async def search_smart(message: types.Message):
    counter = 0
    scraper = AllShopsScraper()
    lst = scraper.get_data()
    for item in lst:
        item['price'] = item['price'].split(' ')
        item['price'] = ''.join(item['price'])
        item['price'] = int(item['price'])
        if 'digital' not in item['name'].lower() and item['price'] <= 2900 or 'digital' not in item['name'].lower() and item['price'] <= 3100 and item['name'].count('+') >= 2 or 'digital' in item['name'].lower() and item['price'] <= 2600 or 'digital' in item['name'].lower() and item['price'] <= 2800 and ('dualsense' or 'pulse 3d') in item['name'].lower() or 'digital' not in item['name'].lower() and item['price'] <= 3200 and ('dualsense' or 'pulse 3d') in item['name'].lower() or 'digital' not in item['name'].lower() and item['price'] <= 3300 and ('dualsense' and 'pulse 3d') in item['name'].lower() or 'digital' in item['name'].lower() and item['price'] <= 3000 and ('dualsense' and 'pulse 3d') in item['name'].lower():
            counter += 1
            await bot.send_message(chat_id=message.from_user.id, text=f"{item['name']} - {item['price']} - {item['link']}")
        if counter == 0:
            await message.answer('Нема гарячих пиріжків(( Заходьте в другий раз!')


@dp.message_handler(commands='radar')
async def set_radar_mode(message: types.Message):
    counter = 0
    while True:
        scraper = AllShopsScraper()
        if counter == 0:
            lst1 = []
            counter += 1
        lst = scraper.get_data()
        for item in lst:
            item['price'] = str(item['price']).split(' ')
            item['price'] = ''.join(item['price'])
            item['price'] = item['price'].strip('zł')
            item['price'] = item['price'].split(',')
            item['price'] = ''.join(item['price'])
            item['price'] = int(item['price'])
            if 'digital' not in item['name'].lower() and item['price'
            ] <= 2900 or 'digital' not in item['name'].lower() and item['price'
            ] <= 3100 and item['name'].count('+') >= 2 or 'digital' in item['name'
            ].lower() and item['price'] <= 2600 or 'digital' in item['name'].lower() and item['price'
            ] <= 2800 and ('dualsense' or 'pulse 3d') in item['name'].lower() or 'digital' not in item['name'
            ].lower() and item['price'] <= 3200 and ('dualsense' or 'pulse 3d') in item['name'].lower() or 'digital' not in item['name'
            ].lower() and item['price'] <= 3300 and ('dualsense' and 'pulse 3d') in item['name'
            ].lower() or 'digital' in item['name'].lower() and item['price'
            ] <= 3000 and ('dualsense' and 'pulse 3d') in item['name'].lower():
                    # counter += 1
                if item not in lst1:
                    await bot.send_message(chat_id=message.from_user.id,
                                            text=f"{item['name']} - {item['price']} - {item['link']}")
        lst1 = lst
                # if counter == 0:
                #     await message.answer("Нема гарячих пиріжків(( Повідомлю як з'являться")

        # while True:
        #     scraper = AllShopsScraper()
        #     lst1 = scraper.get_data()
        #     for item in lst:
        #         item['price'] = item['price'].split(' ')
        #         item['price'] = ''.join(item['price'])
        #         item['price'] = int(item['price'])
        #         if 'digital' not in item['name'].lower() and item['price'] <= 2900 or 'digital' not in item[
        #             'name'].lower() and item['price'] <= 3100 and item['name'].count('+') >= 2 or 'digital' in item[
        #             'name'].lower() and item['price'] <= 2600 or 'digital' in item['name'].lower() and item[
        #             'price'] <= 2800 and ('dualsense' or 'pulse 3d') in item['name'].lower() or 'digital' not in item[
        #             'name'].lower() and item['price'] <= 3200 and ('dualsense' or 'pulse 3d') in item[
        #             'name'].lower() or 'digital' not in item['name'].lower() and item['price'] <= 3300 and (
        #                 'dualsense' and 'pulse 3d') in item['name'].lower() or 'digital' in item['name'].lower() and \
        #                 item[
        #                     'price'] <= 3000 and ('dualsense' and 'pulse 3d') in item['name'].lower():
        #             lst1.append(item)
        #             if item not in lst:
        #                 await bot.send_message(chat_id=message.from_user.id,
        #                                        text=f"{item['name']} - {item['price']} - {item['link']}")
        #
        #     lst = lst1


@dp.message_handler(commands='radar_iphone')
async def set_radar_mode_iphone(message: types.Message):
    counter = 0
    while True:
        time.sleep(10)
        scraper = MediaExpertScraper()
        if counter == 0:
            lst = []
            lst1 = []
            counter += 1
        for page in range(1, scraper.found_last_page(
                'https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/apple') + 1):
            scraper.search_iphone(f'https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/apple?page={page}')
            for item in scraper.products:
                if ('iphone 13 pro 256gb' in item['name'].lower() or 'iphone 13 pro max 128gb' in item['name'].lower()) and item not in lst1:
                    lst.append(item)
                    await bot.send_message(chat_id=message.from_user.id, text=f"{item['name']} - {item['price']} - {item['link']}")
            lst1 = lst







if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
