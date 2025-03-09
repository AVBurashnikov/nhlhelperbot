import random
from telegram import Update, Message
from telegram.ext import CallbackContext
import logging

from api_fetcher import handle_api_response
from api_models.summary import Summary
from urls import Urls

logger = logging.getLogger("nhlapi.bot")


async def unfollow_handler(update: Update, context: CallbackContext, game_id: int) -> None:
    jobs = context.job_queue.get_jobs_by_name(f"follow_{game_id}")
    if not jobs:
        await update.message.reply_text(f"Этот матч не отслеживается.")
        return

    message: Message = jobs[0].data["message"]
    jobs[0].schedule_removal()
    logger.info(f"Match {game_id} tracking stopped.")


async def follow_handler(update: Update, context: CallbackContext, game_id: int) -> None:
    jobs = context.job_queue.get_jobs_by_name(f"follow_{game_id}")
    if not jobs:
        message = await update.message.reply_text(
            f"Запущено отслеживание матча {game_id} запущено, "
            f"оно прекратится по окончании. Загружаю данные..."
        )

        context.job_queue.run_repeating(
            callback=follow_game,
            interval=random.randint(5,15),
            first=1,
            name=f"follow_{game_id}",
            data={
                "update": update,
                "message": message,
                "game_id": game_id
            }
        )
    else:
        logger.warning("Tracking for this match is already running")
        await update.message.reply_text(f"Отслеживание этого матча уже запущено.")


async def follow_game(context: CallbackContext):
    update: Update = context.job.data["update"]
    message: Message = context.job.data["message"]
    game_id: int = context.job.data["game_id"]

    await handle_api_response(
        update,
        context,
        Summary,
        Urls.build_url("game_summary", game_id),
        game_summary_builder,
        message,
        True
    )
