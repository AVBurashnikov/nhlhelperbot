from telegram import Update
from telegram.ext import CallbackContext

from builders.records import records_builder
from message import send_message


async def records_handler(update: Update, context: CallbackContext) -> None:
    await send_message(update, records_builder())
