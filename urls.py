from typing import Any, Optional


class Urls:
    _urls = {
        "schedule": "https://api-web.nhle.com/v1/schedule/%s",
        "score": "https://api-web.nhle.com/v1/score/now",
        "standings": "https://api-web.nhle.com/v1/standings/now",
        "stats": "https://api-web.nhle.com/v1/%s-stats-leaders/%s/%s?limit=%s",
        "player_landing": "https://api-web.nhle.com/v1/player/%s/landing",
        "game_summary": "https://api-web.nhle.com/v1/gamecenter/%s/landing",
        "right_rail": "https://api-web.nhle.com/v1/gamecenter/%s/right-rail",
        "roster": "https://api-web.nhle.com/v1/roster/%s/current",
        "team_schedule": "https://api-web.nhle.com/v1/scoreboard/%s/now",
        # goalie records url
        "goalie-records": "https://records.nhl.com/site/api/goalie-career-stats?"
                          "cayenneExp=gameTypeId=2 and gamesPlayed>=100 and "
                          "franchiseId=null&sort=[{'property':'gamesPlayed','direction':'DESC'},"
                          "{'property':'lastName','direction':'ASC_CI'}]"

    }

    @staticmethod
    def build_url(key: str, *args) -> str:
        try:
            url_template = Urls._urls.get(key)
            if url_template is None:
                raise KeyError(f"Key '{key}' not found in Urls._urls")
            url = url_template % args
            return url
        except (KeyError, TypeError, AttributeError, ValueError, IndexError) as e:
            print(f"Error occurred: {e}")
            return ""
