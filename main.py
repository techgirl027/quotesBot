from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="7018120596:AAG8sDGkzZrZcod6rxG92jHpfjxpTQs9KK4")
dp = Dispatcher(bot)

data = [
    {
        "id": 1,
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
    },
    {
        "id": 2,
        "quote": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs",
    },
    {"id": 3, "quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
]


@dp.message_handler(commands=["start"])
async def greating(message: types.Message):
    await message.answer(f"Assalomu alaykum! {message.from_user.full_name}")


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    help_text = f"Bu bot kunlik iqtiboslar yuboradi.\nadmin:@n_nematjonova"
    await message.reply(help_text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def set_bot_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushirish"),
            types.BotCommand("help", "Yordam"),
        ]
    )


async def on_startup(dp: Dispatcher):
    await set_bot_commands(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
