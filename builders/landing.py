from api_models.player_landing import PlayerLanding
from api_models.player_stats_by_season import PlayerStatsBySeason
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    code,
    italic,
    underline,
    safe_team_info)
from helpers.constants import COUNTRY, FIELD_POSITION
from typing import Callable
from helpers.timelib import calculate_age


def player_profile_builder(data: PlayerLanding) -> str:
    """Строит профиль игрока в зависимости от его позиции."""
    return _goalie_profile(data) if data.position == "G" else _skater_profile(data)


def _build_player_header(player: PlayerLanding) -> str:
    """Создает заголовок профиля игрока."""
    return _(
        [
            _([
                _(player.sweater_number, post=". "),
                COUNTRY.get(player.birth_country, "N/A"),
                _([
                    player.first_name.default,
                    player.last_name.default
                ], fmt_func=bold),
                _([
                    safe_team_info(player.current_team_abbrev, "icon"),
                    player.current_team_abbrev,
                ], pre="(", post=")", new_line=2),
                _("🥅" if player.position == "G" else "🏒"),
                _(FIELD_POSITION.get(player.position, ""), fmt_func=italic),
            ], new_line=1),
            _([
                _(["Возраст", calculate_age(player.birth_date)], sep=":"),
                _(["Рост", player.height], sep=":"),
                _(["Вес", player.weight], sep=":")
            ], fmt_func=code)
        ],
        new_line=2
    )


def build_stat_section(header: str, stats: PlayerStatsBySeason, stat_formatter: Callable[[PlayerStatsBySeason], str]) -> str:
    """Создает секцию статистики с заголовком и отформатированными данными."""
    return _(header, fmt_func=(underline, italic)) + stat_formatter(stats)


def _skater_profile(skater: PlayerLanding) -> str:
    """Создает профиль полевого игрока."""
    return _build_athlete_profile(skater, skater_stat_formatter)


def _goalie_profile(goalie: PlayerLanding) -> str:
    """Создает профиль вратаря."""
    return _build_athlete_profile(goalie, goalie_stat_formatter)


def _build_athlete_profile(player: PlayerLanding, formatter: Callable[[PlayerStatsBySeason], str]) -> str:
    """Строит профиль игрока (общий для полевых игроков и вратарей)."""
    if player.featured_stats is None:
        return _(
            "Этот игрок пока не обладает статистикой в НХЛ."
        )

    return _([
        _build_player_header(player),
        _("Статистика в NHL", fmt_func=bold, new_line=2),
        build_stat_section(
            _("В текущем сезоне(за карьеру):", new_line=1),
            player.featured_stats.regular_season,
            formatter
        )
    ])


def goalie_stat_formatter(stats: PlayerStatsBySeason) -> str:
    """Форматирует статистику вратаря."""
    return _(
        [
            _([
                _get_stats_as_str(stats, "games_played"),
                "игр сыграно"
            ]),
            _([
                f"{stats.current_season.gaa:.2f}",
                f"({stats.career.gaa:.2f})",
                "в среднем пропущено за матч"
            ]),
            _([
                _get_stats_as_str(stats, "wins"),
                "побед"
            ]),
            _([
                _get_stats_as_str(stats, "losses"),
                "поражений"
            ]),
            _([
                _get_stats_as_str(stats, "ot_losses"),
                "поражений в ОТ"
            ]),
            _([
                f"{stats.current_season.save_pctg:.2%}",
                f"({stats.current_season.save_pctg:.2%})",
                "процент отраженных бросков"
            ]),
            _([
                _get_stats_as_str(stats, "shutouts"),
                "сухих матчей"
            ])
        ], sep="\n", new_line=2)


def skater_stat_formatter(stats: PlayerStatsBySeason) -> str:
    """Форматирует статистику полевого игрока."""
    return _([
            _([
                _get_stats_as_str(stats, "games_played"),
                "игр сыграно"
            ]),
            _([
                _get_stats_as_str(stats, "goals"),
                "голов"
            ]),
            _([
                _get_stats_as_str(stats, "winning_goals"),
                "победных голов"
            ]),
            _([
                _get_stats_as_str(stats, "ot_goals"),
                "голов в овертаймах"
            ]),
            _([
                _get_stats_as_str(stats, "assists"),
                "передач"
            ]),
            _([
                _get_stats_as_str(stats, "points"),
                "очков"
            ]),
            _([
                _get_stats_as_str(stats, "plus_minus"),
                "плюс-минус"
            ]),
            _([
                _get_stats_as_str(stats, "penalty_minutes"),
                "штрафных минут"
            ]),
            _([
                _get_stats_as_str(stats, "shots"),
                "бросков"
            ]),
            _([
                f"{getattr(stats.current_season, 'shooting_pctg', 0.0):.1%}",
                f"({getattr(stats.career, 'shooting_pctg', 0.0):.1%})",
                "процент точных бросков"
            ])
        ], sep="\n", new_line=2)


def _get_stats_as_str(stats: PlayerStatsBySeason, attr: str) -> str:
    return _([
        getattr(stats.current_season, attr),
        f"({getattr(stats.career, attr)})"
    ])
