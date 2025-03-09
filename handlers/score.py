from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.score import Score
from builders.score import score_builder
from urls import Urls


async def score_handler(update: Update, context: CallbackContext) -> None:
    await handle_api_response(
        update,
        context,
        Score,
        Urls.build_url("score"),
        score_builder,
        "score",
    )