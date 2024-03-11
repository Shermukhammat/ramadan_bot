import pytz
from datetime import datetime


def get_now(zone : str = 'Asia/Tashkent'):
    zone_tz = pytz.timezone(zone)
    now = datetime.now(zone_tz)

    return datetime(now.year, now.month, now.day)

def is_ramadan(now : datetime, start : datetime = datetime(2024, 3, 11), end : datetime = datetime(2024, 4, 9)):
    return start <= now and now <= end

def convert_now_to_str(now : datetime):
    return now.strftime("%Y-%m-%d")

now = get_now()
print(is_ramadan(now))

print(now.strftime("%Y-%m-%d"))