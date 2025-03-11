from telegram import Update
from telegram.ext import CallbackContext

from builders.trophy import trophy_help_builder
from message import send_message


async def trophy_handler(update: Update, context: CallbackContext) -> None:
    message = trophy_help_builder()
    for chunk in message:
        print(chunk[:30], f"{len(chunk)=}")
        await send_message(update, chunk)
