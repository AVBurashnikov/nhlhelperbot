from enum import Enum
from typing import NewType

SeasonId = NewType("SeasonId", int)


class Seasons:
    PREV_SEASON: SeasonId = SeasonId(20232024)
    CURRENT_SEASON: SeasonId = SeasonId(20242025)
    NEXT_SEASON: SeasonId = SeasonId(20252026)


class GameTypes(Enum):
    REGULAR: int = 2
    PLAY_OFF: int = 3

DECISION = {
    "O": "❌ Поражение в ОТ",
    "W": "✅ Победа",
    "L": "❌ Поражение",
}

FIELD_POSITION = {
    "G": "Вратарь",
    "D": "Защитник",
    "L": "Левый нападающий",
    "C": "Центральный нападающий",
    "R": "Правый нападающий",
}

GAME_STATE = {
    'FUT': '(Скоро)',
    'PRE': '(Перед началом)',
    'LIVE': '(Онлайн)',
    'CRIT': '(Завершается)',
    'FINAL': '(Окончание)',
    'OFF': '(Завершен)'
}

TEAMS_ABBR = {
    "wsh": {
        "place_name": "Washington",
        "common_name": "Capitals",
        "icon": "🦅"
    },
    "wpg": {
        "place_name": "Winnipeg",
        "common_name": "Jets",
        "icon": "🛩"
    },
    "vgk": {
        "place_name": "Vegas",
        "common_name": "Golden Knights",
        "icon": "🛡"
    },
    "edm": {
        "place_name": "Edmonton",
        "common_name": "Oilers",
        "icon": "🛢"
    },
    "car": {
        "place_name": "Carolina",
        "common_name": "Hurricanes",
        "icon": "🌪"
    },
    "tor": {
        "place_name": "Toronto",
        "common_name": "Maple Leafs",
        "icon": "🍁"
    },
    "min": {
        "place_name": "Minnesota",
        "common_name": "Wild",
        "icon": "🐻"
    },
    "njd": {
        "place_name": "New Jersey",
        "common_name": "Devils",
        "icon": "😈"
    },
    "dal": {
        "place_name": "Dallas",
        "common_name": "Stars",
        "icon": "⭐️"
    },
    "fla": {
        "place_name": "Florida",
        "common_name": "Panthers",
        "icon": "🐯"
    },
    "col": {
        "place_name": "Colorado",
        "common_name": "Avalanche",
        "icon": "🗻"
    },
    "lak": {
        "place_name": "Los Angeles",
        "common_name": "Kings",
        "icon": "👑"
    },
    "bos": {
        "place_name": "Boston",
        "common_name": "Bruins",
        "icon": "🏵"
    },
    "tbl": {
        "place_name": "Tampa Bay",
        "common_name": "Lightning",
        "icon": "⚡️"
    },
    "cgy": {
        "place_name": "Calgary",
        "common_name": "Flames",
        "icon": "🔥"
    },
    "cbj": {
        "place_name": "Columbus",
        "common_name": "Blue Jackets",
        "icon": "👔"
    },
    "nyr": {
        "place_name": "New York",
        "common_name": "Rangers",
        "icon": "🗽"
    },
    "ott": {
        "place_name": "Ottawa",
        "common_name": "Senators",
        "icon": "👲"
    },
    "mtl": {
        "place_name": "Montréal",
        "common_name": "Canadiens",
        "icon": "🇨🇦"
    },
    "van": {
        "place_name": "Vancouver",
        "common_name": "Canucks",
        "icon": "🐋"
    },
    "stl": {
        "place_name": "St. Louis",
        "common_name": "Blues",
        "icon": "🎷"
    },
    "phi": {
        "place_name": "Philadelphia",
        "common_name": "Flyers",
        "icon": "👨🏻‍✈️"
    },
    "uta": {
        "place_name": "Utah",
        "common_name": "Hockey Club",
        "icon": "🧢"
    },
    "det": {
        "place_name": "Detroit",
        "common_name": "Red Wings",
        "icon": "🐦‍🔥"
    },
    "pit": {
        "place_name": "Pittsburgh",
        "common_name": "Penguins",
        "icon": "🐧"
    },
    "nyi": {
        "place_name": "New York",
        "common_name": "Islanders",
        "icon": "🏝"
    },
    "sea": {
        "place_name": "Seattle",
        "common_name": "Kraken",
        "icon": "🐙"
    },
    "ana": {
        "place_name": "Anaheim",
        "common_name": "Ducks",
        "icon": "🦆"
    },
    "nsh": {
        "place_name": "Nashville",
        "common_name": "Predators",
        "icon": "🐆"
    },
    "buf": {
        "place_name": "Buffalo",
        "common_name": "Sabres",
        "icon": "🦬"
    },
    "chi": {
        "place_name": "Chicago",
        "common_name": "Blackhawks",
        "icon": "🪶"
    },
    "sjs": {
        "place_name": "San Jose",
        "common_name": "Sharks",
        "icon": "🦈"
    },
    "usa": {
        "place_name": "United States",
        "common_name": "",
        "icon": "🇺🇸"
    },
    "can": {
        "place_name": "Canada",
        "common_name": "",
        "icon": "🇨🇦"
    },
    "swe": {
        "place_name": "Sweden",
        "common_name": "",
        "icon": "🇸🇪"
    },
    "fin": {
        "place_name": "Finland",
        "common_name": "",
        "icon": "🇫🇮"
    },
    "rus": {
        "place_name": "Russia",
        "common_name": "",
        "icon": "🇷🇺"
    }
}

COUNTRY = {
    "RUS": "🇷🇺",
    "USA": "🇺🇸",
    "CAN": "🇨🇦",
    "CZE": "🇨🇿",
    "SVK": "🇸🇰",
    "SLO": "🇸🇮",
    "FIN": "🇫🇮",
    "SWE": "🇸🇪",
    "GER": "🇩🇪",
    "BLR": "🇧🇾",
    "SUI": "🇨🇭",  # Швейцария
    "CHE": "🇨🇭",  # Швейцария
    "AUT": "🇦🇹",  # Австрия
    "FRA": "🇫🇷",
    "ITA": "🇮🇹",
    "ESP": "🇪🇸",
    "GBR": "🇬🇧",
    "CHN": "🇨🇳",
    "JPN": "🇯🇵",
    "KOR": "🇰🇷",
    "BRA": "🇧🇷",
    "ARG": "🇦🇷",
    "MEX": "🇲🇽",
    "IND": "🇮🇳",
    "AUS": "🇦🇺",  # Австралия
    "NZL": "🇳🇿",
    "ZAF": "🇿🇦",
    "NGA": "🇳🇬",
    "EGY": "🇪🇬",
    "SAU": "🇸🇦",
    "TUR": "🇹🇷",
    "UKR": "🇺🇦",
    "POL": "🇵🇱",
    "NLD": "🇳🇱",
    "BEL": "🇧🇪",
    "PRT": "🇵🇹",
    "GRC": "🇬🇷",
    "ISR": "🇮🇱",
    "THA": "🇹🇭",
    "IDN": "🇮🇩",
    "MYS": "🇲🇾",
    "PHL": "🇵🇭",
    "VNM": "🇻🇳",
    "PAK": "🇵🇰",
    "BGD": "🇧🇩",
    "IRN": "🇮🇷",
    "IRQ": "🇮🇶",
    "AFG": "🇦🇫",
    "KAZ": "🇰🇿",
    "UZB": "🇺🇿",
    "TJK": "🇹🇯",
    "KGZ": "🇰🇬",
    "TKM": "🇹🇲",
    "AZE": "🇦🇿",
    "GEO": "🇬🇪",
    "ARM": "🇦🇲",
    "ISL": "🇮🇸",
    "NOR": "🇳🇴",
    "DNK": "🇩🇰",
    "EST": "🇪🇪",
    "LVA": "🇱🇻",
    "LAT": "🇱🇻",
    "LTU": "🇱🇹",
    "IRL": "🇮🇪",
    "LUX": "🇱🇺",
    "CYP": "🇨🇾",
    "MLT": "🇲🇹",
    "ALB": "🇦🇱",
    "MKD": "🇲🇰",
    "BIH": "🇧🇦",
    "SRB": "🇷🇸",
    "MNE": "🇲🇪",
    "HRV": "🇭🇷",
    "BGR": "🇧🇬",
    "ROU": "🇷🇴",
    "HUN": "🇭🇺",
    "SVN": "🇸🇮",
    "CUB": "🇨🇺",
    "JAM": "🇯🇲",
    "DOM": "🇩🇴",
    "PRI": "🇵🇷",
    "COL": "🇨🇴",
    "VEN": "🇻🇪",
    "PER": "🇵🇪",
    "CHL": "🇨🇱",
    "ECU": "🇪🇨",
    "BOL": "🇧🇴",
    "PRY": "🇵🇾",
    "URY": "🇺🇾",
    "CRI": "🇨🇷",
    "PAN": "🇵🇦",
    "NIC": "🇳🇮",
    "HND": "🇭🇳",
    "SLV": "🇸🇻",
    "GTM": "🇬🇹",
    "HTI": "🇭🇹",
    "CYM": "🇰🇾",
    "BRB": "🇧🇧",
    "TTO": "🇹🇹",
    "SUR": "🇸🇷",
    "GUY": "🇬🇾",
    "FLK": "🇫🇰",
    "SGP": "🇸🇬",
    "BRN": "🇧🇳",
    "KHM": "🇰🇭",
    "LAO": "🇱🇦",
    "MMR": "🇲🇲",
    "LKA": "🇱🇰",
    "NPL": "🇳🇵",
    "BTN": "🇧🇹",
    "MDV": "🇲🇻",
    "FSM": "🇫🇲",
    "WSM": "🇼🇸",
    "TON": "🇹🇴",
    "VUT": "🇻🇺",
    "SLB": "🇸🇧",
    "PNG": "🇵🇬",
    "ATA": "🇦🇶",  # Антарктида
    "ATF": "🇹🇫",  # Французские Южные территории
    "SGS": "🇬🇸",  # Южная Георгия и Южные Сандвичевы острова
    "HMD": "🇭🇲",  # Остров Херд и острова Макдональд
    "UMI": "🇺🇲",  # Внешние малые острова США
    "PCN": "🇵🇳",  # Острова Питкэрн
    "SPM": "🇵🇲",  # Сен-Пьер и Микелон
    "MAF": "🇲🇫",  # Сен-Мартен
    "BLM": "🇧🇱",  # Сен-Бартелеми
    "SHN": "🇸🇭",  # Остров Святой Елены
    "TCA": "🇹🇨",  # Острова Тёркс и Кайкос
    "AIA": "🇦🇮",  # Ангилья
    "VGB": "🇻🇬",  # Британские Виргинские острова
    "VIR": "🇻🇮",  # Виргинские острова США
    "MSR": "🇲🇸",  # Монтсеррат
    "KNA": "🇰🇳",  # Сент-Китс и Невис
    "DMA": "🇩🇲",  # Доминика
    "GRD": "🇬🇩",  # Гренада
    "LCA": "🇱🇨",  # Сент-Люсия
    "VCT": "🇻🇨",  # Сент-Винсент и Гренадины
    "ABW": "🇦🇼",  # Аруба
    "CUW": "🇨🇼",  # Кюрасао
    "SXM": "🇸🇽",  # Синт-Мартен
    "BES": "🇧🇶",  # Бонайре, Синт-Эстатиус и Саба
    "GLP": "🇬🇵",  # Гваделупа
    "MTQ": "🇲🇶",  # Мартиника
    "REU": "🇷🇪",  # Реюньон
    "MYT": "🇾🇹",  # Майотта
    "GUF": "🇬🇫",  # Французская Гвиана
    "ATB": "🇦🇹",  # Австрия (уже есть "AUS" для Австралии)
    "AND": "🇦🇩",  # Андорра
    "LIE": "🇱🇮",  # Лихтенштейн
    "MCO": "🇲🇨",  # Монако
    "SMR": "🇸🇲",  # Сан-Марино
    "VAT": "🇻🇦",  # Ватикан
    "MNP": "🇲🇵",  # Северные Марианские острова
    "GUM": "🇬🇺",  # Гуам
    "ASM": "🇦🇸",  # Американское Самоа
    "MHL": "🇲🇭",  # Маршалловы острова
    "PLW": "🇵🇼",  # Палау
    "NRU": "🇳🇷",  # Науру
    "TUV": "🇹🇻",  # Тувалу
    "KIR": "🇰🇮",  # Кирибати
    "COK": "🇨🇰",  # Острова Кука
    "NIU": "🇳🇺",  # Ниуэ
    "TKL": "🇹🇰",  # Токелау
    "WLF": "🇼🇫",  # Уоллис и Футуна
    "PYF": "🇵🇫",  # Французская Полинезия
    "NCL": "🇳🇨",  # Новая Каледония
}
