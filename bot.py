import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ChatMemberStatus
from pydantic.v1.class_validators import all_kwargs

from config import TOKEN

CHANEL = "@inomov_22"


dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def is_sub(bot, chanel, id):
    user = await bot.get_chat_member(chanel, id)
    if user.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]:
        return False

    return True


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    is_subscribe = await is_sub(bot, CHANEL, message.from_user.id)

    if is_subscribe:
        await message.answer("Xush kelibsiz!")
    else:
        await message.answer(f"{CHANEL} ga obuna bo'ling")



@dp.message()
async def echo_handler(message: Message) -> None:
    is_s = await is_sub(bot, CHANEL, message.from_user.id)
    if not is_s:
        await message.answer("Botda foydalanishdan avval regist")
        return
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls


    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())