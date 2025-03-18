from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.most_stats import MostStats
from builders.most import most_builder
from builders.records import records_builder
from message import send_message
from urls import Urls


async def records_handler(update: Update, context: CallbackContext) -> None:
    await send_message(update, records_builder())


async def most_handler(update: Update, context: CallbackContext, category: str, period: str = "") -> None:
    await handle_api_response(
        update,
        context,
        MostStats,
        Urls.build_url("skaters-records", category, category),
        lambda model: most_builder(model, category, period),
        f"most-{category}-{period}"
    )
