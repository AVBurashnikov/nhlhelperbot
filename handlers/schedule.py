from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.schedule import Schedule
from builders.schedule import schedule_builder
from helpers.timelib import now
from urls import Urls


async def schedule_handler(update: Update, context: CallbackContext) -> None:
    await handle_api_response(
        update,
        context,
        Schedule,
        Urls.build_url("schedule", now(-1)),
        schedule_builder,
        "schedule_query",
    )
