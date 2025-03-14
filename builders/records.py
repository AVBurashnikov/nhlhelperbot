from helpers.formatters import format_command, bold
from helpers.text_builder import text as _


def records_builder() -> str:
    return _([
        _("Основные рекорды НХЛ", pre="📊", fmt_func=bold, new_line=2),
        format_command(
            "most",
            "goals",
            description="🎯 Наибольшее количество заброшенных шайб",
            new_line=2
        ),
        format_command(
            "most",
            "assists",
            description="🤝 Наибольшее число ассистов",
            new_line=2
        ),
        format_command(
            "most",
            "points",
            description="🎯 Наибольшее количество очков",
            new_line=2
        ),
        format_command(
            "most",
            "games",
            description="Наибольшее количество сыгранных игр",
            new_line=2
        )
    ])
