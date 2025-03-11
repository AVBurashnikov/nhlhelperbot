from handlers.commands import COMMANDS
from helpers.formatters import format_divider, format_command, bold, italic
from helpers.text_builder import text as _


def help_builder() -> str:
    """Сборщик help'а."""
    help_message = [
        _("📚 Справка по командам бота NHLHelper", fmt_func=bold, new_line=2),
        _("📍 Основные команды:", fmt_func=bold, new_line=1),
        _("/start - 🚀 Начало работы с ботом", new_line=1),
        _("/schedule - 📅 Расписание матчей на два дня вперед", new_line=1),
        _("/scores - 🏆 Результаты прошедшего игрового дня", new_line=1),
        _("/team_abbrev - 🏳️ Список аббревиатур команд (например, /TBL)", new_line=1),
        _("/roster - 📋 Список команд для вызова состава", new_line=1),
        _("/roster_&lt;аббревиатура команды&gt; - 👥 Текущий состав указанной команды (например, /TBL_roster)", new_line=1),
        _("/skater_stats - 🏌️‍♂️ Статистика по очкам ТОП-10 лиги", new_line=1),
        _("/goalie_stats - 🥅 Статистика по вратарям (процент отраженных бросков ТОП-10)", new_line=1),
        _("/standings - 🏅 Текущее положение команд в лиге", new_line=2),
        format_divider(),
        _("📍 Дополнительные команды:", fmt_func=bold, new_line=1),
    ]

    # Добавляем информацию о командах из словаря COMMANDS
    for command, info in COMMANDS.items():
        description = info.get("description", "Нет описания")
        usage = format_command(command, "...") if info.get("min_args", 0) > 0 else f"/{command}"
        emoji = "⚙️"  # Общий эмодзи для дополнительных команд
        help_message.append(_(f"{emoji} {usage} - {description}", new_line=1))

    help_message.extend([
        format_divider(),
        _("📍 Примеры использования команд:", fmt_func=bold, new_line=1),
        _("• /TBL - 📅 Расписание игр Tampa Bay Lightning", new_line=1),
        _("• /TBL_roster - 👥 Текущий состав Tampa Bay Lightning", new_line=1),
        _("• /pl_8471214 - 🏌️‍♂️ Профиль игрока с ID 8471214", new_line=1),
        _("• /g_2023020001 - 🏒 Сводка матча с ID 2023020001", new_line=1),
        _("• /watch_2023020001 - 🔍 Начать отслеживание матча с ID 2023020001", new_line=1),
        _("• /unwatch_2023020001 - ❌ Прекратить отслеживание матча с ID 2023020001", new_line=2),
        _("💡 Подсказка: Используйте команды с параметрами для получения точной информации!", fmt_func=italic, new_line=1)
    ])

    return _(help_message)
