import datetime, math

a = input()
b = input()

def parse_date(date: str):
    date_str, tz_str = date.split()
    sign = 1 if tz_str[3] == "+" else -1
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    hours_offset = int(tz_str[4:6])
    min_offset = int(tz_str[7:])
    diff = datetime.timedelta(hours = hours_offset, minutes = min_offset) * sign
    dt_utc = dt - diff
    return dt_utc

date1 = parse_date(a)
date2 = parse_date(b)


days = abs((date1 - date2).total_seconds()/86400)
print(math.floor(days))