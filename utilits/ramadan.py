import pytz
from datetime import datetime, timedelta


def get_now(zone : str = 'Asia/Tashkent'):
    zone_tz = pytz.timezone(zone)
    now = datetime.now(zone_tz)

    return datetime(now.year, now.month, now.day)

def get_tmorow(zone : str = 'Asia/Tashkent'):
    zone_tz = pytz.timezone(zone)
    now = datetime.now(zone_tz)

    tmorow = datetime(now.year, now.month, now.day) + timedelta(days = 1)
    return datetime(tmorow.year, tmorow.month, tmorow.day)

def is_ramadan(now : datetime, start : datetime = datetime(2024, 3, 11), end : datetime = datetime(2024, 4, 9)):
    return start <= now and now <= end

def convert_now_to_str(now : datetime):
    return f"{now.year}-{now.month}-{now.day}"