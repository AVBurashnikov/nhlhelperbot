from telegram import Update
from telegram.ext import CallbackContext
import logging

from handlers.game_summary import game_summary_handler


logger = logging.getLogger("nhlapi.bot")


def game_watch_handler(update: Update, context: CallbackContext, game_id: int):
    job = context.job_queue.run_repeating(
        callback=_game_watch_callback,
        interval=60,
        first=1,
        name=f"game_watch_{game_id}",
        data={
            "update": update,
            "game_id": game_id,
            "watch": True
        }
    )
    if job:
        logger.info(f"Match tracking started. Job name is {job.name}.")


def game_unwatch_handler(update: Update, context: CallbackContext, game_id: int):
    ...


async def _game_watch_callback(context: CallbackContext):
    await game_summary_handler(
        update=context.job.data["update"],
        context=context,
        game_id=context.job.data["game_id"],
        watch=context.job.data["watch"]
    )