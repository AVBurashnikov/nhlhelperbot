import logging

from telegram import Update
from telegram.ext import CallbackContext
from message import send_message
from builders.start import start_builder


logger = logging.getLogger("nhlapi.bot")


async def start_handler(update: Update, context: CallbackContext) -> None:
    logger.info(f"NEW USER. {update.message.from_user.first_name} "
                f"{update.message.from_user.last_name} join the bot!")
    await send_message(
        update,
        start_builder()
    )
