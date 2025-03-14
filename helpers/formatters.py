from typing import (
    NewType,
    Callable,
    Any,
    Optional
)

from api_models.assist import Assist
from api_models.goal import Goal
from api_models.penalty_info import PenaltyInfo
from api_models.shootout import Shootout
from api_models.star import Star
from api_models.team import Team
from api_models.player import Player
from helpers.text_builder import text as _
from helpers.constants import TEAMS_ABBR, COUNTRY, GAME_STATE
from helpers.timelib import to_msc_datetime

HTMLString = NewType('HTMLString', str)


def bold(value: Any) -> HTMLString:
    return HTMLString(f"<b>{value}</b>")


def italic(value: Any) -> HTMLString:
    return HTMLString(f"<i>{value}</i>")


def underline(value: Any) -> HTMLString:
    return HTMLString(f"<u>{value}</u>")


def strike(value: Any) -> HTMLString:
    return HTMLString(f"<s>{value}</s>")


def cite(value: Any) -> HTMLString:
    return HTMLString(f"<blockquote>{value}</blockquote>")


def code(value: Any) -> HTMLString:
    return HTMLString(f"<code>{value}</code>")


def spoiler(value: Any) -> HTMLString:
    return HTMLString(f"<span class='tg-spoiler'>{value}</span>")


def link(value: Any, anchor: str) -> HTMLString:
    return HTMLString(f"<a href='{anchor}'>{value}</a>")


def message_header(header: str, pre: str = "", post: str = "") -> str:
    return _(header, pre=pre, post=post, fmt_func=bold, new_line=2)


def get_time_emoji(time) -> str:
    if not time:
        return ""
    hour, minute = map(int, time.split(':'))
    hour = hour if hour <= 12 else hour - 12

    if minute == 0:
        return f"🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"[hour % 12]
    elif minute == 30:
        return f"🕧🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦"[hour % 12]
    return ""


def get_team_name(team: Team) -> str:
    return _(
        get_team_display_name(team)
    )


def safe_team_info(team_abbrev: str, key: str) -> str:
    """Безопасное получение информации о команде"""
    return TEAMS_ABBR.get(team_abbrev.lower(), {}).get(key, "N/A")


def safe_game_state(game_state: str) -> str:
    return GAME_STATE.get(game_state, "N/A")


def safe_team_abbrev(team: Team) -> str:
    if isinstance(team.abbrev, str):
        return team.abbrev
    return team.team_abbrev.default


def safe_get_flag(birth_country: str) -> str:
    return COUNTRY.get(birth_country, "N/A")


def get_team_display_name(team: Team) -> str:
    """Форматирует название команды с учетом исключений для Rangers/Islanders"""
    abbrev = safe_team_abbrev(team)
    common_name = safe_team_info(abbrev, "common_name")
    place_name = safe_team_info(abbrev, "place_name")
    return common_name if common_name in ("Islanders", "Rangers") else place_name


def format_player_name(player: Player) -> str:
    return _([
        f"{player.sweater_number}",
        safe_get_flag(player.birth_country) if player.birth_country else "",
        player.first_name.default,
        player.last_name.default
    ], fmt_func=bold)


def format_match(away: Team, home: Team, game_id: int = 0) -> str:
    abbrev_away = safe_team_abbrev(away)
    abbrev_home = safe_team_abbrev(home)
    return _(
        _([
            _([
                safe_team_info(abbrev_away, "icon"),
                get_team_display_name(away),
            ]),
            _([
                safe_team_info(abbrev_home, "icon"),
                get_team_display_name(home),
            ])
        ], sep=" - ")
    )


def format_datetime(date: str, date_only: bool = False, time_only: bool = False, new_line: int = 1) -> str:
    if date_only:
        return _(to_msc_datetime(date, date_only=True), fmt_func=code, new_line=new_line)
    if time_only:
        return _(to_msc_datetime(date, time_only=True), pre="[", post="]", fmt_func=bold, new_line=new_line)
    return _(to_msc_datetime(date), fmt_func=code, new_line=new_line)


def format_score(away: Team, home: Team, show_sog: bool = False) -> str:
    if show_sog:
        return _([
            f"({away.sog}) {away.score} - {home.score} ({home.sog})"
        ])
    return _([
        f"{away.score} - {home.score}"
    ])


def format_divider(new_line: int = 1) -> str:
    return _("—" * 10, new_line=new_line)


def format_goal(goal: Goal) -> str:
    return _([
        _(goal.time_in_period),
        _("(PowPl)" if goal.strength == "pp" else ""),
        _("(EmpNet)" if goal.goal_modifier == "empty-net" else ""),
        format_team_abbrev(goal.team_abbrev.default, only_icon=True),
        _(goal.name.default, fmt_func=bold),
        _(goal.goals_to_date, pre="(", post=")"),
        _([goal.away_score, goal.home_score], sep="-"),
        format_command("pl", goal.player_id),
    ], pre="🎯", new_line=1)


def format_assist(assist: Assist) -> str:
    return _([
        assist.name.default,
        f"({assist.assists_to_date})",
        format_command("pl", assist.player_id),
    ], pre="❗️", fmt_func=italic, new_line=1)


def format_shootout(shootout: Shootout) -> str:
    return _([
        _("✅" if shootout.result == "goal" else "❌"),
        _(shootout.first_name.default),
        _(shootout.last_name.default),
        format_team_abbrev(shootout.team_abbrev.default),
        format_command("pl", shootout.player_id),
    ], new_line=1)


def format_penalty(penalty: PenaltyInfo) -> str:
    served_by = penalty.served_by.default if penalty.served_by else penalty.player_name.default
    return _([
        _(penalty.time_in_period),
        _(format_team_abbrev(penalty.team_abbrev.default, only_icon=True)),
        _(served_by, fmt_func=bold),
        _(penalty.description, pre="(", post=")")
    ], new_line=1)


def format_match_star(star: Star, index: int) -> str:
    star_markers = ["1️⃣", "2️⃣", "3️⃣"]
    return _([
        star_markers[index],
        f"({star.position})",
        format_team_abbrev(star.team_abbrev, only_icon=True),
        _(star.name.default, fmt_func=bold),
        star.save_pctg if star.position == "G" else f"{star.goals} + {star.assists}"
    ], new_line=1)


def format_team_abbrev(abbrev: str, only_icon: bool = False, func: Optional[Callable] = None) -> str:
    team_abbrev = [
        safe_team_info(abbrev, "icon"),
        abbrev if not only_icon else "",
    ]

    if func is not None and callable(func):
        return _(team_abbrev, sep="", fmt_func=func)
    return _(team_abbrev, sep="")


def format_team_icon(abbrev: str) -> str:
    """Возвращает строку с иконками команд"""
    return f"{TEAMS_ABBR[abbrev]['icon']}"


def format_command(*args: Any, description: str = "", new_line: int = 0):
    if description:
        return _([
            f"/{'_'.join(map(str, args))}",
            description
        ], sep=" - ", new_line=new_line)
    return _(f"/{'_'.join(map(str, args))}", new_line=new_line)
