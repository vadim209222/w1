from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.types import CallbackQuery
from keyboards import main_kb, payment_kb


token = 'BOT TOKEn'
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    user_id = message.chat.id
    await message.answer(f'Приветствую, {username}!\n\n'
                         'Это закрытый клуб по подписке. \nОстался всего один шаг для доступа!'
                         ' а также помогу с оплатой,На канале будет размещаться информация по '
                         'саморазвитию и мотивации, советы и практики как поддерживать здоровый образ жизни, '
                         'регулярно заниматься спортом, придерживаться здорового питания, также будут размещаться'
                         ' видео с тренировками, рекомендации книг и фильмов по теме. \n\nФорма оплаты — подписка с '
                         'автоматическим продлением.\nПереходя к оплате, Вы соглашаетесь с условиями '
                         'публичной оферты\nПрисоединиться👇🏻', reply_markup=main_kb)


@dp.callback_query_handler(lambda query: query.data == 'join')
async def process_join_callback(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id,'Рада, что вы решили стать частью нашей команды\n\n'
                         'Нажимаем на кнопку "подписка на 30 дней" указываем номер телефона и оплачиваем,'
                         'после успешной оплаты перед вами появится кнопка "join group" -> Поздравляю, вы стали частью нашей семьи ❤️\n\n'
                         'Стоимость активации подписки 900р/месяц \n',
                         reply_markup=payment_kb)
    # удаление сообщения предыдущей команды
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
