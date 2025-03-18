from helpers.formatters import format_command, bold
from helpers.text_builder import text as _


def records_builder() -> str:
    return _([
        _("Основные рекорды НХЛ", pre="📊", fmt_func=bold, new_line=2),
        format_command(
            "most",
            "goals",
            "rs",
            description="Наибольшее количество заброшенных шайб за регулярный сезон",
            new_line=1
        ),
        format_command(
            "most",
            "goals",
            "po",
            description="Наибольшее количество заброшенных шайб в плейофф",
            new_line=1
        ),
        format_command(
            "most",
            "goals",
            description="Наибольшее количество заброшенных шайб за карьеру",
            new_line=1
        ),
        format_command(
            "most",
            "assists",
            "rs",
            description="Наибольшее число ассистов в регулярных сезонах",
            new_line=1
        ),
        format_command(
            "most",
            "assists",
            "po",
            description="Наибольшее число ассистов в плейофф",
            new_line=1
        ),
        format_command(
            "most",
            "assists",
            description="Наибольшее число ассистов за карьеру",
            new_line=1
        ),
        format_command(
            "most",
            "points",
            "rs",
            description="Наибольшее количество очков в регулярных сезонах",
            new_line=1
        ),
        format_command(
            "most",
            "points",
            "po",
            description="Наибольшее количество очков в плейофф",
            new_line=1
        ),
        format_command(
            "most",
            "points",
            description="Наибольшее количество очков за карьеру",
            new_line=1
        ),
        format_command(
            "most",
            "games",
            description="Наибольшее количество сыгранных игр",
            new_line=1
        )
    ])
