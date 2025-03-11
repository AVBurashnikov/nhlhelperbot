from telegram import Update
from telegram.ext import CallbackContext
from api_fetcher import handle_api_response
from api_models.summary import Summary
from builders.game_summary import game_summary_builder
from urls import Urls


async def game_summary_handler(update: Update, context: CallbackContext, game_id: int, watch: bool = False) -> None:
    await handle_api_response(
        update,
        context,
        Summary,
        Urls.build_url("game_summary", game_id),
        game_summary_builder,
        f"game_summary_{game_id}",
        300,
        watch
    )