from typing import List

from api_models.award import Award
from api_models.player_landing import PlayerLanding
from api_models.player_stats_by_season import PlayerStatsBySeason

from helpers.text_builder import text as _
from helpers.formatters import bold, code, italic, underline, safe_team_info, format_divider, format_datetime, \
    format_command, cite
from helpers.constants import COUNTRY, FIELD_POSITION, DECISION
from helpers.timelib import calculate_age


def player_profile_builder(player_landing: PlayerLanding) -> str:
    """Строит профиль игрока в зависимости от его позиции."""
    return _([
        _build_player_header(player_landing),
        _("Статистика в NHL",pre="📊", fmt_func=bold, new_line=1),
        format_divider(),
        _("В текущем сезоне(за карьеру):", fmt_func=(underline, italic), new_line=1),
        _build_player_stat(
            player_landing.featured_stats.regular_season,
            player_landing.position
        ),
        _("Предыдущие 5 матчей:", pre="📝", fmt_func=(underline, italic), new_line=1),
        _build_player_last_5_stat(
            player_landing,
            player_landing.position
        ),
        _("Награды", fmt_func=bold, new_line=1),
        format_divider(),
        _build_player_awards(player_landing.awards),
        _(f"💡 Подсказка: Используйте команду {format_command("trophy")} для "
          f"получения справки по трофеям!",
          fmt_func=italic, new_line=1)
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
            ], pre="⚔️"),
            _([
                _(f"{stats.current_season.gaa:.2f}({stats.career.gaa:.2f})", fmt_func=bold),
                "в среднем пропущено за матч"
            ], pre="🥅"),
            _([
                _get_stats_as_str(stats, "wins"),
                "побед"
            ], pre="✅"),
            _([
                _get_stats_as_str(stats, "losses"),
                "поражений"
            ], pre="❌"),
            _([
                _get_stats_as_str(stats, "ot_losses"),
                "поражений в ОТ"
            ], pre="⏱"),
            _([
                _([
                    f"{stats.current_season.save_pctg:.2%}",
                    f"({stats.career.save_pctg:.2%})",
                ], fmt_func=bold),
                "процент отраженных бросков"
            ], pre="🛡"),
            _([
                _get_stats_as_str(stats, "shutouts"),
                "сухих матчей"
            ], pre="💯")
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
        ], pre="⚔️"),
        _([
            _get_stats_as_str(stats, "goals"),
            "голов"
        ], pre="🎯"),
        _([
            _get_stats_as_str(stats, "winning_goals"),
            "победных голов"
        ], pre="🎯"),
        _([
            _get_stats_as_str(stats, "ot_goals"),
            "голов в овертаймах"
        ], pre="🎯"),
        _([
            _get_stats_as_str(stats, "assists"),
            "передач"
        ], pre="🤝"),
        _([
            _get_stats_as_str(stats, "points"),
            "очков"
        ], pre="🎲"),
        _([
            _get_stats_as_str(stats, "plus_minus"),
            "плюс-минус"
        ], pre="-/+"),
        _([
            _get_stats_as_str(stats, "penalty_minutes"),
            "штрафных минут"
        ], pre="👎🏻"),
        _([
            _get_stats_as_str(stats, "shots"),
            "бросков"
        ], pre="🎯"),
        _([
            _([
                f"{getattr(stats.current_season, 'shooting_pctg', 0.0):.1%}",
                f"({getattr(stats.career, 'shooting_pctg', 0.0):.1%})",
            ], fmt_func=bold),
            "процент точных бросков"
        ], pre="🔬")
    ], sep="\n", new_line=2)


def _skater_last5_formatter(player: PlayerLanding) -> str:
    games = []
    for game in player.last_5_games:
        games.append(
            _([
                format_datetime(game.game_date, date_only=True),
                safe_team_info(game.opponent_abbrev, "icon"),
                _(game.opponent_abbrev),
                _([
                    "Очки:",
                    _(f"{game.goals}+{game.assists}", fmt_func=bold)
                ]),
                _(format_command("g", game.game_id)),
            ], new_line=2)
        )
    return _(games)


def _build_player_awards(awards: List[Award]):

    def _format_season(season: int) -> str:
        season_str = str(season)
        return f"{season_str[:4]}/{season_str[4:]}"

    if awards is None:
        return _("Наград пока нет.", new_line=2)

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
    award_items.append(_(new_line=1))
    return _(award_items)


def _build_player_header(player: PlayerLanding) -> str:
    """Создает заголовок профиля игрока."""
    if player.position == "G":
        details = _goalie_details(player)
    else:
        details = _skater_details(player)
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
        _(FIELD_POSITION.get(player.position, ""), fmt_func=italic, new_line=2),
        details
    ], new_line=2)


def _goalie_details(player: PlayerLanding) -> str:
    save_pctg_record = max([
        season.save_pctg if season.league_abbrev == "NHL" else 0 for season in player.season_totals
    ])
    return _([
        _("Личный рекорд(отр.броски):"),
        _(f"{save_pctg_record:.2%}", fmt_func=bold, new_line=1),
        _in_team_since(player)
    ])


def _skater_details(player: PlayerLanding) -> str:
    points_record = max([
        season.points if season.league_abbrev == "NHL" else 0 for season in player.season_totals
    ])
    return _([
        _("Личный рекорд(гол+пас):"),
        _(points_record, fmt_func=bold, new_line=1),
        _in_team_since(player)
    ])


def _in_team_since(player: PlayerLanding) -> str:

    season_totals = [season for season in player.season_totals if season.league_abbrev == "NHL"]

    team_name = season_totals[-1].team_name.default
    year = str(season_totals[-1].season)[:4]

    for season in season_totals[::-1]:
        if team_name == season.team_name.default:
            year = str(season.season)[:4]
        else:
            break

    return _([
        _("Команда:"),
        _(team_name, fmt_func=bold),
        _("c"),
        _(year, fmt_func=bold),
        _("г.")
    ])


def _get_stats_as_str(stats: PlayerStatsBySeason, attr: str) -> str:
    return _([
        getattr(stats.current_season, attr),
        f"({getattr(stats.career, attr)})"
    ], fmt_func=bold)
