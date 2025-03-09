from telegram import Update
from telegram.ext import CallbackContext

from api_fetcher import handle_api_response
from api_models.schedule_team import ScheduleTeam
from builders.schedule import team_schedule_builder
from urls import Urls


async def team_schedule_handler(
        update: Update,
        context: CallbackContext,
        team_name: str) -> None:

    await handle_api_response(
        update,
        context,
        ScheduleTeam,
        Urls.build_url("team_schedule", team_name),
        lambda model: team_schedule_builder(model, team_name.lower()),
        f"{team_name}_schedule",
    )