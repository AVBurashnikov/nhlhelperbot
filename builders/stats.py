from typing import List

from api_models.stats import Stats, Player
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    format_player_name,
    format_command,
    format_team_abbrev,
    message_header
)


def stats_block(header: str, players: List[Player]) -> str:
    leaders = [header]
    for player in players:
        leaders.append(
            _([
                _(f"{player.value:.3%}" if player.position == "G" else player.value, fmt_func=bold),
                format_team_abbrev(player.team_abbrev),
                format_player_name(player),
                format_command("pl", player.player_id)
            ], new_line=1)
        )

    return _(leaders)


def goalie_stats_builder(data: Stats) -> str:
    return stats_block(
        message_header("Лидеры по проценту отраженных бросков", pre="⛔️"),
        data.save_pctg
    )


def skater_stats_builder(data: Stats) -> str:
    return stats_block(
        message_header("Лидеры по очкам", pre="🏅"),
        data.points
    )


def stats_builder(data: Stats, player: str = "skater") -> str:
    return skater_stats_builder(data) if player == "skater" else goalie_stats_builder(data)