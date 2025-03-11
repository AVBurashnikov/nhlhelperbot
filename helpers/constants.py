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


TROPHY_LIST = {
    # Командные трофеи
    "Stanley Cup": {
        "descr": "Награждается команда выигравшая финальную "
                 "серию плей-офф с 1927 года. С 1893 по 1914 "
                 "годы вручался лучшей любительской команде Канады. "
                 "В период с 1915 по 1926 годы обладателем "
                 "становилась команда выигравшая серию между "
                 "чемпионами НХЛ и НХА",
        "since": 1893
    },
    "Prince of Wales Trophy": {
        "descr": "Награждается команда-чемпион Восточной конференции. "
                 "До этого вручалась чемпиону НХЛ (1924—1927), чемпиону "
                 "Американского дивизиона (1928—1938), победителю "
                 "регулярного чемпионата (1939—1967), чемпиону Восточного "
                 "дивизиона (1968—1974), чемпиону Конференции принца "
                 "Уэльского (1975—1993)",
        "since": 1925
    },
    "Clarence S. Campbell Bowl": {
        "descr": "Награждается команда-чемпион Западной конференции с 1994 "
                 "года. Ранее вручался чемпиону Западного дивизиона (1968–1974) "
                 "и Конференции Кэмпбелла (1975–1993)",
        "since": 1968
    },
    "Presidents' Trophy": {
        "descr": "Награждается команда набравшая большее количество очков в "
                 "регулярном чемпионате",
        "since": 1986
    },
    "O'Brien Trophy": {
        "descr": "Награждался победитель плей-офф НХА и НХЛ (1910–23), чемпион "
                 "Канадского дивизиона (1927–38), а затем финалист Кубка Стэнли "
                 "(1939–50).",
        "since": 1910
    },

    # Индивидуальные трофеи
    "Hart Memorial Trophy": {
        "descr": "Награждается игрок, который внёс наибольший вклад в "
                 "успехи своей команды в регулярном чемпионате.",
        "since": 1924
    },
    "Lady Byng Memorial Trophy": {
        "descr": "Награждается игрок, продемонстрировавший образец "
                 "честной спортивной борьбы и джентльменского "
                 "поведения в сочетании с высоким игровым мастерством.",
        "since": 1925
    },
    "Vezina Trophy": {
        "descr": "Награждается голкипер, сыгравший в регулярном "
                 "чемпионате не менее 25 матчей и продемонстрировавший "
                 "лучшую игру среди всех конкурентов.",
        "since": 1927
    },
    "Calder Memorial Trophy": {
        "descr": "Награждается игрок, наиболее ярко проявивший себя "
                 "среди тех, кто проводит первый полный сезон в составе "
                 "клуба НХЛ.",
        "since": 1937
    },
    "Art Ross Trophy": {
        "descr": "Награждается игрок, набравший наибольшее количество "
                 "очков по системе гол+пас в регулярном чемпионате.",
        "since": 1948
    },
    "James Norris Memorial Trophy": {
        "descr": "Награждается защитник, который проявил наибольшее "
                 "мастерство при игре на своей позиции на протяжении "
                 "всего сезона.",
        "since": 1954
    },
    "Conn Smythe Trophy": {
        "descr": "Награждается игрок, лучше других зарекомендовавший "
                 "себя в играх плей-офф.",
        "since": 1965
    },
    "Bill Masterton Memorial Trophy": {
        "descr": "Награждается игрок, проявивший высокое спортивное "
                 "мастерство и верность хоккею.",
        "since": 1968
    },
    "Ted Lindsay Award": {
        "descr": "Награждается игрок, лучший по мнению самих хоккеистов. "
                 "Приз учрежден Ассоциацией хоккеистов НХЛ (NHLPA) в честь "
                 "Лестера Пирсона, бывшего премьер-министра Канады. 29 "
                 "апреля 2010 года НХЛ переименовала трофей в честь хоккеиста "
                 "Теда Линдсея.",
        "since": 1971
    },
    "Jack Adams Award": {
        "descr": "Награждается тренер, внесший наибольший вклад в успехи "
                 "своей команды, по мнению Ассоциации журналистов НХЛ.",
        "since": 1974
    },
    "Frank J. Selke Trophy": {
        "descr": "Награждается лучший нападающий оборонительного плана.",
        "since": 1978
    },
    "William M. Jennings Trophy": {
        "descr": "Награждается голкипер(ы), пропустивший(е) наименьшее "
                 "число голов в среднем за игру по итогам регулярного "
                 "сезона при не менее 25 сыгранных матчах.",
        "since": 1982
    },
    "King Clancy Memorial Trophy": {
        "descr": "Награждается игрок, который является примером для "
                 "партнеров на льду и вне его и принимает активное "
                 "участие в общественной жизни.",
        "since": 1988
    },
    "Maurice “Rocket” Richard Trophy": {
        "descr": "Награждается игрок, забросивший наибольшее число шайб "
                 "среди всех игроков НХЛ по итогам регулярного сезона.",
        "since": 1999
    },
    "Mark Messier NHL Leadership Award": {
        "descr": "Приз вручается Марком Мессье игроку проявившему "
                 "лидерские качества на льду и за его пределами",
        "since": 2007
    },
    "Jim Gregory General Manager of the Year Award": {
        "descr": "Награждается генеральный менеджер, внесший "
                 "наибольший вклад в успехи своей команды.",
        "since": 2010
    },
    "Willie O'Ree Community Hero Award": {
        "descr": "Приз за позитивное влияние при помощи хоккея.",
        "since": 2018
    },
    "NHL Plus-Minus Award": {
        "descr": "Награждался игрок с лучшим показателем «плюс-минус» "
                 "по итогам регулярного сезона.",
        "since": 1983,
        "stopped": 2008,
        "last": "Павел Дацюк"
    },
    "Roger Crozier Saving Grace Award": {
        "descr": "Награждался голкипер с лучшим процентом отраженных "
                 "бросков, сыгравший не менее 25 матчей.",
        "since": 2000,
        "stopped": 2007,
        "last": "Никлас Бэкстрём"
    },
    "NHL Foundation Player Award": {
        "descr": "Приз игроку за участие в благотворительности.",
        "since": 1998,
        "stopped": 2018,
        "last": "Трэвис Хамоник"
    },
    "E. J. McGuire Award of Excellence": {
        "descr": "Премия имени Э. Дж. Макгуайра за выдающиеся "
                 "достижения ежегодно вручается перспективному "
                 "игроку драфта Национальной хоккейной лиги, который "
                 "наилучшим образом демонстрирует «стремление к "
                 "совершенству через силу характера, конкурентоспособность "
                 "и атлетизм», выбранному Центральным скаутским бюро "
                 "НХЛ на драфте НХЛ. Премия названа в честь бывшего "
                 "директора Центрального скаутского бюро НХЛ Э. Дж. Макгуайра.",
        "since": 2015,
    }
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
