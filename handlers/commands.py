from typing import Dict, Callable, Awaitable, List

from telegram import Update
from telegram.ext import CallbackContext
# Импорт обработчиков
from handlers.game_summary import game_summary_handler
from handlers.game_watch import game_watch_handler, game_unwatch_handler
from handlers.player_landing import player_command_handler
from handlers.records import most_handler
from handlers.standings import standings_handler


# Определение типа обработчика команды
CommandHandler = Callable[
    [Update, CallbackContext, List[str]],
    Awaitable[None]
]

# Словарь команд с их обработчиками и требованиями к аргументам
COMMANDS: Dict[str, Dict[str, CommandHandler | int | str]] = {
    "pl": {
        "handler": player_command_handler,
        "min_args": 1,
        "description": "Профиль игрока"
    },
    "g": {
        "handler": game_summary_handler,
        "min_args": 1,
        "description": "Подробности матча"
    },
    "standings": {
        "handler": standings_handler,
        "min_args": 0,
        "description": "Турнирная таблица"
    },
    "watch": {
        "handler": game_watch_handler,
        "min_args": 1,
        "description": "Следить за матчем с указанным ID"
    },
    "unwatch": {
        "handler": game_unwatch_handler,
        "min_args": 1,
        "description": "Прекратить следить за матчем с указанным ID"
    },
    "most": {
        "handler": most_handler,
        "min_args": 1,
        "description": "Рекорд НХЛ"
    }
}