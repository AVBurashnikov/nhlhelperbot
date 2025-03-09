from typing import List

from api_models.award import Award
from api_models.player_landing import PlayerLanding
from api_models.player_stats_by_season import PlayerStatsBySeason

from helpers.text_builder import text as _
from helpers.formatters import bold, code, italic, underline, safe_team_info, format_divider, format_datetime, \
    format_command
from helpers.constants import COUNTRY, FIELD_POSITION, DECISION
from helpers.timelib import calculate_age


def player_profile_builder(player_landing: PlayerLanding) -> str:
    """Строит профиль игрока в зависимости от его позиции."""
    return _([
        _build_player_header(player_landing),
        _("Статистика в NHL", fmt_func=bold, new_line=1),
        format_divider(),
        _("В текущем сезоне(за карьеру):", fmt_func=(underline, italic), new_line=1),
        _build_player_stat(
            player_landing.featured_stats.regular_season,
            player_landing.position
        ),
        _("Предыдущие 5 матчей:", fmt_func=(underline, italic), new_line=1),
        _build_player_last_5_stat(
            player_landing,
            player_landing.position
        ),
        _("Награды", fmt_func=bold, new_line=1),
        format_divider(),
        _build_player_awards(player_landing.awards)
    ])


def _build_player_stat(player_stat: PlayerStatsBySeason, position: str) -> str:
    if position == "G":
        return _goalie_stat_formatter(player_stat)
    return _skater_stat_formatter(player_stat)


def _build_player_last_5_stat(player: PlayerLanding, position: str) -> str:
    if position == "G":
        return _goalie_last5_formatter(player)
    return _skater_last5_formatter(player)


def _goalie_stat_formatter(stats: PlayerStatsBySeason) -> str:
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


def _goalie_last5_formatter(player: PlayerLanding) -> str:
    save_pctg = player.featured_stats.regular_season.current_season.save_pctg

    games = []
    for game in player.last_5_games:
        games.append(
            _([
                format_datetime(game.game_date, date_only=True),
                _(DECISION.get(game.decision, "N/A"), fmt_func=bold),
                _("против"),
                safe_team_info(game.opponent_abbrev, "icon"),
                _(game.opponent_abbrev),
                _(format_command("g", game.game_id), new_line=1),
                _([
                    f"Пропущено:",
                    "💯" if game.goals_against == 0 else "",
                    f"{game.goals_against}",
                    f"({game.shots_against})",
                    f"{game.save_pctg:.2%}",
                    _("📈" if game.save_pctg > save_pctg else "📉")
                ]),
            ], new_line=2)
        )
    return _(games)


def _skater_stat_formatter(stats: PlayerStatsBySeason) -> str:
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


def _skater_last5_formatter(player: PlayerLanding) -> str:
    games = []
    for game in player.last_5_games:
        games.append(
            _([
                format_datetime(game.game_date, date_only=True),
                # text(DECISION.get(game.decision, "N/A"), fmt_func=bold),
                # text("Против"),
                safe_team_info(game.opponent_abbrev, "icon"),
                _(game.opponent_abbrev),
                _(format_command("g", game.game_id), new_line=1),
                _([
                    "Очки:",
                    _(f"{game.goals}+{game.assists}", fmt_func=bold)
                ])
            ], new_line=2)
        )
    return _(games)


def _build_player_awards(awards: List[Award]):

    def _format_season(season: int) -> str:
        season_str = str(season)
        return f"{season_str[:4]}/{season_str[4:]}"

    if awards is None:
        return _("Наград пока нет.")

    award_items = []
    for award in awards:
        award_items.append(
            _([
                _(award.trophy.default, fmt_func=bold),
                _([
                    _format_season(a.season_id) for a in award.seasons
                ], fmt_func=code)
            ], new_line=1)
        )
    return _(award_items)


def _build_player_header(player: PlayerLanding) -> str:
    """Создает заголовок профиля игрока."""
    return _([
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
            ], pre="(", post=")", new_line=1),
            _([
                _(["Возраст", calculate_age(player.birth_date)], sep=":"),
                _(["Рост", player.height], sep=":"),
                _(["Вес", player.weight], sep=":")
            ], fmt_func=code),
        ], new_line=2),
        _("🥅" if player.position == "G" else "🏒"),
        _(FIELD_POSITION.get(player.position, ""), fmt_func=italic),
    ], new_line=2)


def _get_stats_as_str(stats: PlayerStatsBySeason, attr: str) -> str:
    return _([
        getattr(stats.current_season, attr),
        f"({getattr(stats.career, attr)})"
    ])
