from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.roster import Roster
from builders.roster import team_roster_builder, help_team_roster_builder
from message import send_message
from urls import Urls


async def team_roster_handler(update: Update, context: CallbackContext, team_name: str) -> None:
    await handle_api_response(
        update,
        context,
        Roster,
        Urls.build_url("roster", team_name),
        lambda model: team_roster_builder(model, team_name.lower()),
        f"{team_name}_roster",
    )


async def roster(update: Update, context: CallbackContext) -> None:
    await send_message(update, help_team_roster_builder())
