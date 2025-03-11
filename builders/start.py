from helpers.formatters import format_divider, bold, format_command, italic
from helpers.text_builder import text as _


def start_builder() -> str:
    return _([
        _("Привет!", pre="👋", fmt_func=bold),
        _("Я бот-помощник для получения информации о NHL", new_line=2),
        _("🤖 Я могу показать расписание матчей, результаты, статистику игроков и многое другое.", new_line=2),
        _("👇 Вот что я умею:", fmt_func=bold, new_line=1),
        _("/schedule - 📅 Расписание матчей", new_line=1),
        _("/scores - 🏆 Текущие результаты матчей", new_line=1),
        _("/standings - 🏅 Турнирная таблица", new_line=1),
        _("/skater_stats - 🏌️‍♂️ Показатели топ-10 полевых игроков", new_line=1),
        _("/goalie_stats - 🥅 Показатели топ-10 вратарей", new_line=1),
        _("/roster - 👥 Список команд для получения текущих составов", new_line=1),
        _("/team_abbrev - 🏳️ Список команд и их аббревиатур", new_line=2),
        format_divider(),
        _("💡 Примеры использования:", fmt_func=bold, new_line=1),
        _("— Чтобы узнать расписание команды, введите /team_abbrev, а затем выберите команду (например, /BOS).", new_line=1),
        _("— Чтобы узнать профиль игрока, введите " + format_command("pl", "&lt;ID&gt;") + " (например, /pl_8476453).", new_line=1),
        _("— Чтобы узнать состав команды, введите " + format_command("&lt;TEAM-ABBREV&gt;", "roster") + " (например, /wsh_roster).", new_line=2),
        _("📍 Подробнее о командах: " + format_command("help"), fmt_func=italic, new_line=1)
    ])
