from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.stats import Stats
from builders.stats import stats_builder
from urls import Urls
from helpers.constants import Seasons, GameTypes


async def stats(update: Update, context: CallbackContext, stats_prefix: str, limit: int = 10) -> None:
    await handle_api_response(
        update,
        context,
        Stats,
        Urls.build_url(
            "stats",
            stats_prefix,
            Seasons.CURRENT_SEASON,
            GameTypes.REGULAR.value,
            limit
        ),
        lambda model: stats_builder(model, stats_prefix),
        f"{stats_prefix}_stats",
    )


async def skater_stats_handler(update: Update, context: CallbackContext) -> None:
    await stats(
        update,
        context,
        'skater'
    )


async def goalie_stats_handler(update: Update, context: CallbackContext) -> None:
    await stats(
        update,
        context,
        'goalie'
    )