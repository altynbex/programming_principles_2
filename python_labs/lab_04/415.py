import datetime, math

def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def parse_date(date):
    date_info, tz = date.split()
    dt = datetime.datetime.strptime(date_info, "%Y-%m-%d")
    short_dt = datetime.datetime(year = 2026, month = dt.month, day = dt.day)
    sign = 1 if tz[3] == "+" else -1
    hour_offset = int(tz[4:6])
    min_offset = int(tz[7:])
    dt_utc = short_dt - datetime.timedelta(hours = hour_offset, minutes = min_offset) * sign
    return dt_utc

a = input()
b = input()
d1 = parse_date(a)
d2 = parse_date(b)
diff = (d1 - d2).total_seconds() / 86400
if diff < 0:
    print(math.ceil(diff) + 365)
else:
    print(math.ceil(diff))
