from typing import List
import logging

from telegram import Update
from telegram.ext import CallbackContext

from handlers.commands import COMMANDS
from helpers.constants import TEAMS_ABBR
from message import send_message
from handlers.team import team_command_handler


logger = logging.getLogger("nhlapi.bot")


async def message_handler(update: Update, context: CallbackContext) -> None:
    """Обработка всех входящих сообщений"""
    message = update.message.text
    logger.info(f"Received message: {message}")

    if not message.startswith("/"):
        await handle_unknown_command(update, message)
        return

    await process_command(update, context, message)


async def process_command(update: Update, context: CallbackContext, message: str) -> None:
    """Обработка команды после проверки формата"""
    command_parts = message.strip("/").split("_")
    command = command_parts[0].lower()
    args = command_parts[1:]

    # Сначала проверяем специальные команды
    if command in COMMANDS:
        await handle_standard_command(update, context, command, args)
    elif command in TEAMS_ABBR:
        await handle_team_command(update, context, command, args)
    else:
        await handle_unknown_command(update, message)


async def handle_standard_command(update: Update, context: CallbackContext, command: str, args: List[str]) -> None:
    """Обработка стандартных команд из словаря COMMANDS"""
    cmd_info = COMMANDS[command]
    required_args = cmd_info.get("min_args", 0)

    if len(args) < required_args:
        logger.warning(f"Missing arguments for command: {command}")
        await send_message(update,
                           f"Missing required arguments for command. Usage: /{command}{'_...' if required_args else ''}")
        return

    try:
        await cmd_info["handler"](update, context, *args)
    except Exception as e:
        logger.error(f"Error processing command /{command}: {str(e)}")
        await send_message(update, "An error occurred while processing your request")


async def handle_team_command(update: Update, context: CallbackContext, team_abbr: str, args: List[str]) -> None:
    """Обработка команд, связанных с командами NHL"""
    try:
        if args:
            logger.info(f"Fetching roster for team: {team_abbr.upper()}")
            await team_command_handler(update, context, team_abbr, args[0])
        else:
            logger.info(f"Fetching schedule for team: {team_abbr.upper()}")
            await team_command_handler(update, context, team_abbr)
    except Exception as e:
        logger.error(f"Error processing team command /{team_abbr}: {str(e)}")
        await send_message(update, "Failed to retrieve team information")


async def handle_unknown_command(update: Update, message: str) -> None:
    """Обработка неизвестных команд"""
    logger.warning(f"Unknown command received: {message}")
    await send_message(update, "Unknown command. Use /help to see available commands")
