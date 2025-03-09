from telegram import Update
from telegram.ext import CallbackContext

from handlers.follow import follow_handler, unfollow_handler
from handlers.game_summary import game_summary_handler
from handlers.player_landing import player_command_handler
from handlers.standings import standings_handler
from handlers.team import team_command_handler
from message import send_message
import logging
from helpers.constants import TEAMS_ABBR

logger = logging.getLogger("nhlapi.bot")


async def message_handler(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    logger.info(f"Received message: {message}")

    # Проверка на команду
    if not message.startswith("/"):
        await handle_unknown_command(update, message)
        return

    # Разделение команды на части
    command, *args = message.strip("/").split("_")

    # Обработка команды "player"
    if command == "pl":
        if not args:
            logger.warning("Player ID is missing.")
            await send_message(update, "Player ID is missing.")
            return
        logger.info(f"Fetching player profile for ID: {args[0]}")
        await player_command_handler(update, context, args[0])
        return

    if command == "g":
        if not args:
            logger.warning("Game ID is missing.")
            await send_message(update, "Game ID is missing.")
            return
        logger.info(f"Fetching game summary for ID: {args[0]}")
        await game_summary_handler(update, context, args[0])
        return

    if command == "standings":
        if not args:
            logger.info("Fetching position of teams in the league.")
            await standings_handler(update, context)
            return
        logger.info(f"Fetching position of teams depending on {args[0]}.")
        await standings_handler(update, context, args[0])
        return

    # Обработка команд, связанных с командами
    if command.lower() not in TEAMS_ABBR:
        logger.warning(f"Unknown command: {message}")
        await handle_unknown_command(update, message)
    elif args:
        logger.info(f"Fetching team roster for: {command.upper()}")
        await team_command_handler(update, context, command, args[0])
    else:
        logger.info(f"Fetching team schedule for: {command.upper()}")
        await team_command_handler(update, context, command)


async def handle_unknown_command(update: Update, message: str) -> None:
    """Обработка неизвестной команды."""
    await send_message(update, "Я не знаю такой команды.")