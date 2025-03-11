from typing import Optional
from api_models.schedule import Schedule
from api_models.schedule_team import ScheduleTeam
from helpers.constants import GAME_STATE
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    strike,
    italic,
    format_match,
    format_command,
    format_datetime,
    safe_team_info, format_divider, code, format_score,
)


def schedule_builder(data: Schedule) -> str:
    """Собирает сообщение с расписанием игр"""
    if not data.game_week:
        return _("Нет расписания.", fmt_func=strike)

    game_days = data.game_week[1:3]

    schedule = [_("Расписание игр", pre="📝", fmt_func=bold, new_line=2)]

    for day in game_days:
        schedule.append(
            format_datetime(day.date, date_only=True)
        )
        schedule.append(
            format_divider()
        )
        if not day.games:
            schedule.append(
                _("Игр не запланировано", fmt_func=italic, new_line=1)
            )

        cur_time = ""
        for game in day.games:
            start_time = format_datetime(game.start_time_utc, time_only=True)
            show_time = start_time != cur_time

            schedule.append(
                _([
                    start_time if show_time else "",
                    format_match(game.away_team, game.home_team, game.game_id),
                    format_command("g", game.game_id)
                ], new_line=1)
            )
            cur_time = start_time

        schedule.append(
            _(new_line=1)
        )

    return _(schedule, sep="")


def team_schedule_builder(data: ScheduleTeam, team_abbrev: str) -> Optional[str]:
    """Собирает расписание для конкретной команды"""
    games_by_date = data.games_by_date

    schedule = [
        _("Расписание матчей", pre="📝", fmt_func=bold, new_line=2),
        _([
            safe_team_info(team_abbrev, 'icon'),
            safe_team_info(team_abbrev, 'place_name'),
            safe_team_info(team_abbrev, 'common_name')
        ], new_line=2)
    ]

    for date in games_by_date[1:6]:
        for game in date.games:
            schedule.append(
                _([
                    format_datetime(game.start_time_utc, new_line=0),
                    _(GAME_STATE.get(game.game_state, "N/A"), fmt_func=code, new_line=1),
                    format_match(game.away_team, game.home_team),
                    _(format_command("g", game.game_id), new_line=1),
                    _(format_score(game.away_team, game.home_team), new_line=1) if game.game_state == "OFF" else ""
                ], new_line=1)
            )

    return _(schedule)
