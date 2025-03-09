from typing import List

from api_models.standing import Standing
from api_models.team import Team
from helpers.text_builder import text as _
from helpers.formatters import (
    bold,
    format_team_icon,
    get_team_display_name, italic, underline, format_command
)


def standings_builder(data: Standing, detail: str):

    league = _league_build()

    for team in data.teams:
        league.add(team)

        match team.conference_abbrev:
            case "E":
                league.eastern.add(team)
            case "W":
                league.western.add(team)

        match team.division_abbrev:
            case "A":
                league.eastern.atlantic.add(team)
            case "M":
                league.eastern.metropolitan.add(team)
            case "C":
                league.western.central.add(team)
            case "P":
                league.western.pacific.add(team)

    match detail:
        case "league":
            return _([
                league.list(),
                _commands_list()
            ])
        case "conf":
            return _([
                league.eastern.list(),
                league.western.list(),
                _commands_list()
            ])
        case "div":
            return _([
                league.eastern.atlantic.list(),
                league.eastern.metropolitan.list(),
                league.western.central.list(),
                league.western.pacific.list(),
                _commands_list()
            ])
        case "":
            return league.league_build()


class NHLStruct:

    def __init__(self, abbr: str, name: str):
        self.abbr = abbr
        self.name = name
        self.teams = []

    def add(self, team: Team):
        self.teams.append(team)

    def list(self):
        team_list = [
            _(self.name, fmt_func=(underline, italic), new_line=1)
        ]
        for team in self.teams:
            team_list.append(
                _([
                    team.points,
                    format_team_icon(team.team_abbrev.default.lower()),
                    get_team_display_name(team),
                    format_command(team.team_abbrev.default)
                ], new_line=1)
            )
        team_list.append(_(new_line=1))

        return _(team_list)


class Division(NHLStruct):

    def __init__(self, abbr: str, name: str):
        super().__init__(abbr, name)


class Conference(NHLStruct):

    def __init__(
            self,
            abbr: str,
            name: str,
            atlantic: Division = None,
            metropolitan: Division = None,
            central: Division = None,
            pacific: Division = None
    ):
        super().__init__(abbr, name)
        if atlantic is not None:
            self.atlantic = atlantic
        if metropolitan is not None:
            self.metropolitan = metropolitan
        if central is not None:
            self.central = central
        if pacific is not None:
            self.pacific = pacific


class League(NHLStruct):

    def __init__(self, abbr: str, name: str, eastern: Conference, western: Conference):
        super().__init__(abbr, name)
        self.eastern = eastern
        self.western = western

    def league_build(self):
        return _([
            _(self.name, fmt_func=bold, new_line=2),
            _(self.eastern.name, fmt_func=bold, new_line=1),
            self.eastern.atlantic.list(),
            self.eastern.metropolitan.list(),
            _(self.western.name, fmt_func=bold, new_line=1),
            self.western.central.list(),
            self.western.pacific.list(),
            _commands_list()
        ])


def _league_build() -> League:

    atlantic = Division("A", "Атлантический дивизион")
    metropolitan = Division("M", "Столичный дивизион")
    central = Division("C", "Центральный дивизион")
    pacific = Division("P", "Тихоокеанский дивизион")

    eastern = Conference("E", "Восточная конференция", atlantic=atlantic, metropolitan=metropolitan)
    western = Conference("W", "Западная конференция", central=central, pacific=pacific)

    return League("NHL", "Национальная хоккейная лига", eastern, western)


def _commands_list() -> str:
    return _([
        format_command("standings", "league", description="положение команд в лиге"),
        _(new_line=1),
        format_command("standings", "conf", description="положение команд по конференциям"),
        _(new_line=1),
        format_command("standings", "div", description="положение команд по дивизионам"),
    ])
