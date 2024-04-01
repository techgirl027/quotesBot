from aiogram import Bot, Dispatcher, executor, types
import random


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
    {
        "id": 4,
        "quote": "Your time is limited, don't waste it living someone else's life.",
        "author": "Steve Jobs",
    },
    {
        "id": 5,
        "quote": "Design is not just what it looks like and feels like. Design is how it works.",
        "author": "Steve Jobs",
    },
    {
        "id": 6,
        "quote": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas A. Edison",
    },
    {
        "id": 7,
        "quote": "Genius is 1% inspiration, and 99% perspiration.",
        "author": "Thomas A. Edison",
    },
    {
        "id": 8,
        "quote": "The only thing we have to fear is fear itself.",
        "author": "Franklin D. Roosevelt",
    },
    {
        "id": 9,
        "quote": "In the end, it's not the years in your life that count. It's the life in your years.",
        "author": "Abraham Lincoln",
    },
    {
        "id": 10,
        "quote": "Don't judge each day by the harvest you reap but by the seeds that you plant.",
        "author": "Robert Louis Stevenson",
    },
    {
        "id": 11,
        "quote": "The only limit to our realization of tomorrow will be our doubts of today.",
        "author": "Franklin D. Roosevelt",
    },
    {
        "id": 12,
        "quote": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
    },
    {
        "id": 13,
        "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela",
    },
    {
        "id": 14,
        "quote": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney",
    },
    {
        "id": 15,
        "quote": "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do.",
        "author": "Steve Jobs",
    },
    {
        "id": 16,
        "quote": "I am not a product of my circumstances. I am a product of my decisions.",
        "author": "Stephen Covey",
    },
    {
        "id": 17,
        "quote": "Every child is an artist. The problem is how to remain an artist once he grows up.",
        "author": "Pablo Picasso",
    },
    {
        "id": 18,
        "quote": "You can never cross the ocean until you have the courage to lose sight of the shore.",
        "author": "Christopher Columbus",
    },
    {
        "id": 19,
        "quote": "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
        "author": "Maya Angelou",
    },
    {
        "id": 20,
        "quote": "Whether you think you can or you think you can't, you're right.",
        "author": "Henry Ford",
    },
    {
        "id": 21,
        "quote": "The best time to plant a tree was 20 years ago. The second best time is now.",
        "author": "Chinese Proverb",
    },
    {
        "id": 22,
        "quote": "The two most important days in your life are the day you are born and the day you find out why.",
        "author": "Mark Twain",
    },
    {
        "id": 23,
        "quote": "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do.",
        "author": "Mark Twain",
    },
    {
        "id": 24,
        "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela",
    },
    {
        "id": 25,
        "quote": "Your time is limited, don't waste it living someone else's life.",
        "author": "Steve Jobs",
    },
    {
        "id": 26,
        "quote": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
    },
    {
        "id": 27,
        "quote": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
    },
    {
        "id": 28,
        "quote": "Don't watch the clock; do what it does. Keep going.",
        "author": "Sam Levenson",
    },
    {
        "id": 29,
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
    },
    {
        "id": 30,
        "quote": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
    },
    {
        "id": 31,
        "quote": "It is our choices, that show what we truly are, far more than our abilities.",
        "author": "J.K. Rowling",
    },
    {
        "id": 32,
        "quote": "Only put off until tomorrow what you are willing to die having left undone.",
        "author": "Pablo Picasso",
    },
    {
        "id": 33,
        "quote": "If you want to lift yourself up, lift up someone else.",
        "author": "Booker T. Washington",
    },
    {
        "id": 34,
        "quote": "The best revenge is massive success.",
        "author": "Frank Sinatra",
    },
    {
        "id": 35,
        "quote": "You miss 100% of the shots you don’t take.",
        "author": "Wayne Gretzky",
    },
    {
        "id": 36,
        "quote": "The only limit to our realization of tomorrow will be our doubts of today.",
        "author": "Franklin D. Roosevelt",
    },
    {
        "id": 37,
        "quote": "You can't fall if you don't climb. But there's no joy in living your whole life on the ground.",
        "author": "Unknown",
    },
    {
        "id": 38,
        "quote": "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained.",
        "author": "Marie Curie",
    },
    {
        "id": 39,
        "quote": "Do what you can, with what you have, where you are.",
        "author": "Theodore Roosevelt",
    },
    {
        "id": 40,
        "quote": "You must be the change you wish to see in the world.",
        "author": "Mahatma Gandhi",
    },
    {
        "id": 41,
        "quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.",
        "author": "Zig Ziglar",
    },
    {
        "id": 42,
        "quote": "The only way to achieve the impossible is to believe it is possible.",
        "author": "Charles Kingsleigh",
    },
]

kb_menu = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton("Iqtibos📃")]], resize_keyboard=True
)


@dp.message_handler(commands=["start"])
async def greating(message: types.Message):
    await message.answer(
        f"Assalomu alaykum! {message.from_user.full_name}", reply_markup=kb_menu
    )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    help_text = f"Bu bot kunlik iqtiboslar yuboradi.\nadmin:@n_nematjonova"
    await message.reply(help_text)


@dp.message_handler(commands=["admin"])
async def admin(message: types.Message):
    text = "Admin Noilaxon Ne'matjonova. Men bilan bog`lanish uchun @n_nematjonova"
    await message.reply(text)


@dp.message_handler(text="Iqtibos📃")
async def send_quote(message: types.Message):
    id = random.randint(0, 41)
    text = data[id]["quote"]
    await message.answer(text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def set_bot_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushirish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("admin", "Admin bilan aloqa"),
        ]
    )


async def on_startup(dp: Dispatcher):
    await set_bot_commands(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
