from api_models.score import Score, Game
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    spoiler,
    link,
    format_match,
    format_score,
    format_datetime, format_divider, format_command
)


def score_builder(data: Score) -> str:
    """Собирает сообщение с результатами матчей"""
    scores = [
        _("Результаты игрового дня", pre="⚔️", fmt_func=bold, new_line=2),
        format_datetime(data.current_date, date_only=True),
        format_divider()
    ]

    for game in data.games:
        scores.append(game_result_builder(game))
    return _(scores)


def game_result_builder(game: Game) -> str:
    score = [
        _(format_match(game.away_team, game.home_team, game.game_id), new_line=1),
        spoiler(format_score(game.away_team, game.home_team, True)),
        _(format_command("g", game.game_id), new_line=1)
    ]

    if game.three_min_recap:
        score.append(_(link("📹 Обзор матча", f"https://nhl.com{game.three_min_recap}"), new_line=2))
    else:
        score.append(_(new_line=1))

    return _(score)
