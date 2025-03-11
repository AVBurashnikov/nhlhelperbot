from telegram import Update
from telegram.ext import CallbackContext

from handlers.team_roster import team_roster_handler
from handlers.team_schedule import team_schedule_handler


async def team_command_handler(
        update: Update,
        context: CallbackContext,
        team_name: str,
        arg: str = ""
) -> None:
    if arg == "roster":
        await team_roster_handler(update, context, team_name)
    else:
        await team_schedule_handler(update, context, team_name)