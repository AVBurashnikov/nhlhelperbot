from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.standing import Standing
from builders.standing import standings_builder
from urls import Urls


async def standings_handler(update: Update, context: CallbackContext, detail: str = "") -> None:
    await handle_api_response(
        update,
        context,
        Standing,
        Urls.build_url("standings"),
        lambda model: standings_builder(model, detail),
        f"standings_{detail}",
    )