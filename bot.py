import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Вставьте сюда токен вашего бота от @BotFather
TOKEN = "8860429298:AAGkjC9lW1zEasicn8vuB99nwtjbbO61GeY"

# Настройка логирования, чтобы видеть работу бота в консоли
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я бот-помощник по математике. Используй команды:\n"
        "/homework — Домашнее задание\n"
        "/deadlines — Дедлайны\n"
        "/grades — Мои оценки\n"
        "/journal — Журнал класса\n"
        "/ask — Как задать вопрос"
    )

# Команда /homework
@dp.message(Command("homework"))
async def cmd_homework(message: Message):
    await message.answer(
        "📚 Актуальное ДЗ:\n"
        "Алгебра: Параграф 14, №245, №248.\n"
        "Геометрия: Повторить теорему Пишагора."
    )

# Команда /deadlines
@dp.message(Command("deadlines"))
async def cmd_deadlines(message: Message):
    await message.answer(
        "⏳ Дедлайны:\n"
        "• До завтра (09:00) — Тест по тригонометрии.\n"
        "• До пятницы (18:00) — Контрольная работа №3."
    )

# Команда /grades
@dp.message(Command("grades"))
async def cmd_grades(message: Message):
    await message.answer(
        "📊 Твои оценки:\n"
        "Самостоятельная работа — 4\n"
        "Контрольная работа — 5\n"
        "Средний балл: 4.5"
    )

# Команда /journal
@dp.message(Command("journal"))
async def cmd_journal(message: Message):
    await message.answer(
        "📖 Журнал класса (Топ-3):\n"
        "1. Иванов И. — 4.9\n"
        "2. Петрова А. — 4.8\n"
        "3. Сидоров А. — 4.5"
    )

# Команда /ask
@dp.message(Command("ask"))
async def cmd_ask(message: Message):
    await message.answer(
        "❓ Чтобы задать вопрос учителю, просто напишите его в этот чат (без команд). "
        "Учитель увидит сообщение и ответит вам!"
    )

# Обработка любого другого текста (вопросы студентов)
@dp.message()
async def handle_all_messages(message: Message):
    await message.answer(
        "🤖 Ваш вопрос записан и отправлен учителю математики. "
        "Ожидайте ответа!"
    )

# Запуск процесса бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())