from api_models.most_stats import MostStats


def most_builder(most_stats: MostStats, category: str, period: str) -> str:
    return f"{category} {period}"
