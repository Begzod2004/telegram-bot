import wikipedia
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5141000904:AAHgsw6hpNPIh5idA2OWKF1j4imGccVZJKM'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom !\nBu Begzodga tegishli bot!\nMa'lumotlar bazasiga hush kelibsiz\nBu bot sizga istagan narsangiz bo'yicha ma'lumotlar qaytaradi.")
@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday narsa topilmadi")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)