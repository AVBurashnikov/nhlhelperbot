from telegram import Update
from telegram.ext import CallbackContext

from builders.team_abbrev import team_abbrev_builder
from message import send_message


async def team_abbrev_handler(update: Update, context: CallbackContext) -> None:
    await send_message(update, team_abbrev_builder())
