from aiogram import executor
from handlers import dp     # не из config, а именно из handlers, т.к. там он уже обвешан hendlers-ами 


async def bot_start(_):
    print('Бот запущен')

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates = True, on_startup = bot_start)