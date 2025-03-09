from telegram import Update
from telegram.ext import CallbackContext
from api_fetcher import handle_api_response
from api_models.player_landing import PlayerLanding
from builders.player_landing import player_profile_builder
from urls import Urls


async def player_command_handler(update: Update, context: CallbackContext, player_id: str) -> None:
    await handle_api_response(
        update,
        context,
        PlayerLanding,
        Urls.build_url("player_landing", player_id),
        player_profile_builder,
        f"player_landing_{player_id}"  # ключ кэширования
    )
