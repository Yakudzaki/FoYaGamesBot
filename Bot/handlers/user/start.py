from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loguru import logger
from utils.db.db_utils import create_user, user_exists

# Сработает если юзера нет в бд
@dp.message_handler(lambda m: user_exists(m.from_user.id) is False)
async def start(message: types.Message):
    user_id = message.from_user.id
    create_user(user_id)
    await message.answer('Приветик! 👋'
                        '🤖 Я - бот-магазин для заработка! Играя в игры, ты можешь заработать денежки.'
                        '📌 Если хочешь попасть в главное меню со всеми играми и прочими, используй команду /menu.'
                        '💰 Чтобы пополнить свой счет, можешь воспользоваться Яндекс.кассой, Сбербанком или Qiwi.'
                        '❓ Есть вопросы? Не беда! Задавай их командой /report (текст сообщения) и администраторы обязательно ответят тебе как можно быстрее.'
                        '🤔 Не знаешь, как пользоваться ботом? Напиши /help и я подскажу тебе, как начать!'
                        '🤝 А еще, если хочешь заказать похожего бота, свяжись с <a href="https://t.me/Yakudza_Drill">Yakudza</a> или <a href="https://t.me/x_FouR_x">Four</a>')


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Приветик! 👋'
                        '🤖 Я - бот-магазин для заработка! Играя в игры, ты можешь заработать денежки.'
                        '📌 Если хочешь попасть в главное меню со всеми играми и прочими, используй команду /menu.'
                        '💰 Чтобы пополнить свой счет, можешь воспользоваться Яндекс.кассой, Сбербанком или Qiwi.'
                        '❓ Есть вопросы? Не беда! Задавай их командой /report (текст сообщения) и администраторы обязательно ответят тебе как можно быстрее.'
                        '🤔 Не знаешь, как пользоваться ботом? Напиши /help и я подскажу тебе, как начать!'
                        '🤝 А еще, если хочешь заказать похожего бота, свяжись с <a href="https://t.me/Yakudza_Drill">Yakudza</a> или <a href="https://t.me/x_FouR_x">Four</a>')