from typing import List

from api_models.roster import Roster, Player
from helpers.constants import TEAMS_ABBR
from helpers.text_builder import text as _
from helpers.formatters import (
    safe_team_info,
    bold,
    format_player_name,
    code,
    format_command,
    format_divider
)


def team_roster_builder(roster: Roster, team_abbrev: str) -> str:
    header = _([
        _("Tекущий состав", pre="", fmt_func=bold, new_line=2),
        safe_team_info(team_abbrev, "icon"),
        safe_team_info(team_abbrev, "place_name"),
        safe_team_info(team_abbrev, "common_name")
    ], new_line=2)

    return _([
        header,
        _block(roster.forwards, "Нападающие"),
        _block(roster.defensemen, "Защитники"),
        _block(roster.goalies, "Вратари"),
    ])


def _block(position: List[Player], title: str) -> str:
    team_block = [
        _(title, fmt_func=code, new_line=1),
        format_divider()
    ]
    for player in position:
        team_block.append(
            _([
                format_player_name(player),
                format_command("pl", player.player_id)
            ], new_line=1)
        )
    return _(team_block, new_line=1)


def help_team_roster_builder() -> str:
    team_rosters = [
        _(_("Составы команд лиги:", pre="👨🏻‍🏭", fmt_func=bold, new_line=2))
    ]
    for k, v in TEAMS_ABBR.items():
        team_rosters.append(
            _([
                format_command(k.upper(), "roster"),
                _([
                    safe_team_info(k, "icon"),
                    safe_team_info(k, "place_name"),
                    safe_team_info(k, "common_name")
                ], fmt_func=bold, new_line=1),
            ])
        )

    return _(team_rosters)
