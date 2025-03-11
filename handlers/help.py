from telegram import Update
from telegram.ext import CallbackContext

from builders.help import help_builder
from message import send_message


async def help_handler(update: Update, context: CallbackContext) -> None:
    await send_message(
        update,
        help_builder()
    )