from datetime import datetime, timedelta
import pytz


def to_msc_datetime(dt: str, date_only: bool = False, time_only: bool = False):
    try:
        utc_t = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        try:
            utc_t = datetime.strptime(dt, "%Y-%m-%d")
        except ValueError:
            ...
    utc_t = utc_t.replace(tzinfo=pytz.utc)
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_datetime = utc_t.astimezone(moscow_tz)

    if date_only:
        return moscow_datetime.strftime("%d/%m/%Y")

    if time_only:
        return moscow_datetime.strftime("%H:%M")

    return moscow_datetime.strftime("%d/%m/%Y %H:%M")


def tomorrow():
    td = datetime.today()
    tmr = td + timedelta(days=1)
    return tmr.strftime("%Y-%m-%d")


def now(days: int = None):
    td = datetime.today()
    if days is None:
        return td.strftime("%Y-%m-%d")
    return (td + timedelta(days=days)).strftime("%Y-%m-%d")


def calculate_age(birthdate: str) -> str:
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return str(age)
