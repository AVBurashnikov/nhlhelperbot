from typing import List

from api_models.match_info import MatchInfo
from api_models.matchup_leader import Leader
from api_models.penalty import Penalty
from api_models.player import Player
from api_models.score import Score
from api_models.shootout import Shootout
from api_models.star import Star
from api_models.summary import Summary
from api_models.team import Team
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    code,
    strike,
    underline,
    italic,
    format_match,
    format_command,
    format_score,
    safe_team_info,
    safe_game_state,
    format_goal,
    format_assist,
    format_shootout,
    format_match_star,
    format_penalty,
    format_datetime, link,
)
from helpers.timelib import to_msc_datetime


def game_summary_builder(summary: Summary, watch: bool = False) -> str:

    if summary.game_state in {"LIVE", "CRIT"}:
        if watch:
            watch_command = _(format_command("unwatch", summary.game_id))
        else:
            watch_command = _(format_command("watch", summary.game_id))
    else:
        watch_command = ""

    game_summary = [
        _([
            _(format_datetime(summary.date, date_only=True, new_line=0), fmt_func=code),
            watch_command
        ], pre="📅", new_line=1),
        _(safe_game_state(summary.game_state), fmt_func=code, new_line=2),
        _(
            to_msc_datetime(summary.start_time, time_only=True),
            pre="[", post="]",fmt_func=bold
        ),
        _(format_match(summary.away_team, summary.home_team), fmt_func=bold, new_line=1),
        _(format_score(summary.away_team, summary.home_team, True) if summary.game_state not in {"FUT", "PRE"} else "", new_line=2),
    ]

    if summary.game_state in {"FUT", "PRE"} and summary.matchup is not None:
        game_summary.append(_matchup_builder(summary))
    elif summary.summary is not None:
        game_summary.append(_summary_builder(summary.summary))
    else:
        return _("Что то пошло не так!")

    return _(game_summary)


def _matchup_builder(summary: Summary) -> str:
    return _([
        _skaters_comparison_build(summary),
        _goalie_comparison_build(summary),
        _bets_rate()
    ])


def _skaters_comparison_build(summary: Summary) -> str:
    skaters_comparison = [
        _(
            "Лидеры команд в предыдущих 5 встречах:",
            fmt_func=bold,
            new_line=1
        )
    ]

    categories = ["Очки", "Голы", "Голевые передачи"]
    for i, leaders in enumerate(summary.matchup.skater_comparison.leaders):
        skaters_comparison.append(
            _([
                _(categories[i], fmt_func=underline, new_line=1),
                _team_leaders_build(
                    leaders=leaders,
                    away_abbrev=summary.away_team.abbrev,
                    home_abbrev=summary.home_team.abbrev
                )
            ], new_line=1)
        )

    return _(skaters_comparison)


def _goalie_comparison_build(summary: Summary) -> str:
    return _([
        _("Сравнение голкиперов команд:", fmt_func=bold, new_line=1),
        _team_goalie_build(summary.matchup.goalie_comparison.away_team, summary.away_team.abbrev),
        _team_goalie_build(summary.matchup.goalie_comparison.home_team, summary.home_team.abbrev)
    ], new_line=1)


def _bets_rate() -> str:
    bets_rate = [
        _("Средние коэффициенты:", fmt_func=bold, new_line=1),
        _("В разработке", fmt_func=strike)
    ]
    return _(bets_rate)


def _team_goalie_build(team: Team, abbrev: str) -> str:
    goalies = []
    for goalie in team.leaders:
        goalies.append(
            _([
                safe_team_info(abbrev, "icon"),
                _(goalie.name.default, fmt_func=bold),
                _(f"{goalie.record}|{goalie.save_pctg:.1%}"),
                format_command("pl", goalie.leader_id)
            ], new_line=1)
        )

    return _(goalies)


def _team_leaders_build(leaders: Leader, away_abbrev: str, home_abbrev: str) -> str:
    return _([
        _get_team_leader(leaders.away_leader, away_abbrev),
        _get_team_leader(leaders.home_leader, home_abbrev)
    ])


def _get_team_leader(leader: Player, abbrev: str) -> str:
    return _([
        safe_team_info(abbrev, "icon"),
        _(leader.name.default, fmt_func=bold),
        f"({leader.value})",
        format_command("pl", leader.leader_id)
    ], fmt_func=italic, new_line=1)


def _summary_builder(match_info: MatchInfo) -> str:
    return _([
        _summary_goals_builder(match_info.scoring),
        _summary_so_builder(match_info.shootout),
        _summary_penalties_builder(match_info.penalties),
        _summary_threestars_builder(match_info.three_stars)
    ])


def _summary_goals_builder(scoring: List[Score]) -> str:

    has_goals = False
    for period in scoring:
        if period.goals:
            has_goals = True

    if not has_goals:
        return ""

    goals = [
        _("Голы:", fmt_func=bold, new_line=1),
    ]
    for period in scoring:
        if period.goals:
            goals.append(
                _goals_build(period)
            )

    return _(goals)


def _goals_build(score: Score) -> str:

    period_type = "период" if score.period_descr.period_type == "REG" else "овертайм"
    period_number = score.period_descr.number
    period_number = period_number if period_number < 4 else period_number - 3

    goals = [
        _([period_number, period_type], fmt_func=(underline, italic), new_line=1)
    ]

    for goal in score.goals:
        goals.append(
            _([
                format_goal(goal),
                _("Ассистенты:", fmt_func=code, new_line=1)
            ])
        )

        if goal.assists:
            for assist in goal.assists:
                goals.append(format_assist(assist))
        else:
            goals.append(_("нет", new_line=1))

        goals.append(_(new_line=1))

    return _(goals)


def _summary_so_builder(shootouts: List[Shootout]) -> str:

    if not shootouts:
        return ""

    shoots = [_("Серия буллитов:", fmt_func=underline, new_line=1)]
    for shootout in shootouts:
        shoots.append(
            format_shootout(shootout)
        )
    shoots.append(_(new_line=1))

    return _(shoots)


def _summary_penalties_builder(penalties: List[Penalty]) -> str:

    has_penalty = False
    for period in penalties:
        if period.penalties:
            has_penalty = True

    if not has_penalty:
        return ""

    penalty_list = [
        _("Удаления:", fmt_func=bold, new_line=1)
    ]

    for period in penalties:

        if not period.penalties:
            continue

        penalty_list.append(
            _([
                _(period.period_descr.number),
                "период" if period.period_descr.period_type == "REG" else "овертайм"
            ], fmt_func=underline, new_line=1)
        )
        for penalty in period.penalties:
            penalty_list.append(
                format_penalty(penalty)
            )
        penalty_list.append(_(new_line=1))

    return _(penalty_list)


def _summary_threestars_builder(threestars: List[Star]) -> str:

    if not threestars:
        return ""

    stars = [
        _("Три звезды:", fmt_func=bold, new_line=1)
    ]
    for i, star in enumerate(threestars):
        stars.append(format_match_star(star, i))

    return _(stars)
