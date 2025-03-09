from helpers.constants import TEAMS_ABBR
from helpers.formatters import bold, format_command, safe_team_info
from helpers.text_builder import text as _


def team_abbrev_builder() -> str:
    message = [_("Аббревиатуры команд лиги:", pre="🅰️", fmt_func=bold, new_line=2)]
    for abbr in TEAMS_ABBR:
        message.append(
            _([
                format_command(abbr.upper()),
                _([
                    safe_team_info(abbr, "icon"),
                    safe_team_info(abbr, "place_name"),
                    safe_team_info(abbr, "common_name")
                ], fmt_func=bold, new_line=1),
            ])
        )
    return _(message)
